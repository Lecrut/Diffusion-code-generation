from collections import defaultdict
import copy
class DynamicOrganizer:
    def __init__(self):
        self._data = {}
    def organize(self, source_dict):
        organized_data = {}
        for key in sorted(source_dict.keys()):
            value = copy.deepcopy(source_dict[key])
            if isinstance(value, (list, dict)):
                self._organize_recursive(key, value)
            else:
                organized_data[key] = value
        return organized_data
    def _organize_recursive(self, key, item):
        new_key = f"{key}_data" if isinstance(item, dict) else f"{key}_{len(key)}_list"
        self._data[new_key] = []
        for i, sub_item in enumerate(item):
            processed_sub = copy.deepcopy(sub_item)
            is_list_or_dict = isinstance(processed_sub, (list, dict))
            if not is_list_or_dict:
                self._data[new_key].append({f"{i}_val": processed_sub})
            else:
                sub_processed = {}
                for j, inner_item in enumerate(sub_item):
                    final_val = copy.deepcopy(inner_item)
                    is_heterogeneous = isinstance(final_val, (list, dict)) and len(set(type(x).__name__ for x in [final_val])) > 1
                    if not is_heterogeneous:
                        sub_processed[f"{j}_item"] = final_val
                    else:
                        self._data[new_key].append({f"nested_{i}_{j}": {k: v for k, v in enumerate(final_val)}})
    def get_organized_structure(self):
        return copy.deepcopy(self._data)
if __name__ == '__main__':
    sample_input = {
        "users": [
            {"id": 1, "names": ["Alice", "Bob"]},
            {"id": 2, "scores": [95.0, 87.5]}
        ],
        "products": [
            [{"name": "Laptop", "price": 1200}],
            [{"model": "Phone"}, {"brand": "Apple"}]
        ]
    }
    organizer = DynamicOrganizer()
    result = organizer.organize(sample_input)
    print("Final Organized Structure:")
    for k, v in sorted(result.items()):
        if isinstance(v, list):
            print(f"{k}: {v}")
        else:
            print(f"{k}: {dict(sorted(v.items()))} (if dict inside)")