import json
class RobustDataAppender:
    def append(self, data_structure, entry):
        try:
            if not isinstance(entry, dict) and not isinstance(entry, list):
                raise TypeError("Entry must be a dictionary or a list.")
            validated_entry = self.validate_and_convert(entry)
            if isinstance(data_structure, list):
                return data_structure + [validated_entry]
            elif isinstance(data_structure, dict):
                new_data = {**data_structure}
                for key in validated_entry:
                    if key not in new_data or (isinstance(new_data[key], str) and len(new_data[key]) > 0):
                        raise ValueError(f"Key '{key}' conflicts with existing data structure.")
                return {**new_data, **validated_entry}
            else:
                raise TypeError("Data structure must be a list or dictionary.")
        except Exception as e:
            print(f"Error appending entry: {e}")
            return None
    def validate_and_convert(self, entry):
        try:
            if isinstance(entry, str) and not json.loads('"' + entry + '"'):
                raise ValueError("Invalid JSON string.")
            parsed_entry = json.dumps(entry).replace("'", '"')
            cleaned_json = json.loads(parsed_entry)
            return cleaned_json
        except Exception as e:
            print(f"Validation error: {e}")
            return None
if __name__ == '__main__':
    sample_list = [1, 2, 3]
    sample_dict = {"a": "x", "b": "y"}
    new_entry_list = [{"id": 4}, {"id": 5}]
    append_result_list = RobustDataAppender().append(sample_list, new_entry_list)
    new_entry_dict = {"c": "z", "d": "w"}
    append_result_dict = RobustDataAppender().append(sample_dict, new_entry_dict)
    print(f"Updated List: {append_result_list}")
    print(f"Updated Dict: {append_result_dict}")