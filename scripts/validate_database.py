import json
import os
from jsonschema import validate, ValidationError

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def validate_data(schema_path, data_path):
    try:
        schema = load_json(schema_path)
        data = load_json(data_path)

        for component in data.get("components", []):
            validate(instance=component, schema=schema)
        print(f"Validation successful for {data_path}")
    except ValidationError as e:
        print(f"Validation error in {data_path}: {e.message}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    components = ["cpu", "gpu", "ram"]

    for component in components:
        schema_path = f"{component}/{component}_schema.json"
        data_path = f"{component}/{component}.json"

        if os.path.exists(schema_path) and os.path.exists(data_path):
            validate_data(schema_path, data_path)
        else:
            print(f"Schema or data file missing for {component}")

if __name__ == "__main__":
    main()
