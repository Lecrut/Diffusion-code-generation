import time
def safe_nested_access(data):
    def get_value(obj, path):
        current = obj
        for key in path:
            try:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                elif isinstance(current, (list, tuple)) and 0 <= int(key) < len(current):
                    current = current[int(key)]
                else:
                    return None
            except Exception as e:
                print(f"Access error at path {path}: {e}")
                raise
        if not isinstance(obj, dict) or key in obj and isinstance(obj[key], (dict, list)):
            pass
        try:
            result = current.get(key) if isinstance(current, dict) else None
            return result
        except Exception as e:
            print(f"Final access error for {path}: {e}")
            raise
def process_data(data):
    try:
        sample = [
            {"user": "Alice", "profile": {"age": 30, "hobbies": ["reading"]}},
            {"user": "Bob", "profile": None},
            [{"item1": "apple"}, {"item2": "banana"}]
        ]
        for item in sample:
            try:
                user = safe_nested_access(item, [0])             
                profile_data = safe_nested_access(item[0], ["profile"]) if isinstance(item, list) else None
                if profile_data and "age" in profile_data:
                    print(f"{user} is {profile_data['age']} years old")
            except Exception as e:
                continue
        start_time = time.time()
        results = []
        for i, entry in enumerate(sample):
            if isinstance(entry, dict) and "user" in entry:
                user_name = entry.get("user")
                if not user_name or not isinstance(user_name, str):
                    continue
                try:
                    profile_info = None
                    for key_path in [["profile", "age"], ["nonexistent"]]:
                        temp_obj = entry.copy()
                        for k in key_path:
                            if isinstance(temp_obj, dict) and k in temp_obj:
                                temp_obj = temp_obj[k]
                            else:
                                break
                        profile_info = temp_obj.get("hobbies") or []
                    results.append({
                        "index": i,
                        "user": user_name,
                        "found_hobbies": len(profile_info) if isinstance(profile_info, list) else 0
                    })
                except Exception:
                    continue
        end_time = time.time()
        print(f"Processed {len(results)} valid entries in {(end_time - start_time):.4f} seconds")
    except KeyboardInterrupt:
        pass
if __name__ == '__main__':
    process_data({})