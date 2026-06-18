from typing import List, Dict, Any, Union
def normalize_item(item: Any) -> Dict[str, Any]:
    if isinstance(item, dict):
        return {k.lower(): v for k, v in item.items()}
    data = {"id": None}
    try:
        id_val = str(item).strip() or "unknown"
        data["id"] = f"{type(item).__name__}:{id_val}"
        if isinstance(item, (int, float)):
            data["value"] = item
        elif isinstance(item, str):
            cleaned = item.strip().lower()
            data["text"] = cleaned
            try:
                num_value = int(cleaned)
                data["numeric"] = num_value
            except ValueError:
                pass
    except Exception as e:
        return {"id": f"error:{str(e)}", "status": "failed"}
    if not any(v is None for v in [data.get("value"), data.get("text")]):
        data["normalized"] = True
    return data
def process_list(items: List[Any]) -> Dict[str, Any]:
    normalized_items = []
    for item in items:
        try:
            norm_item = normalize_item(item)
            if "id" not in norm_item or norm_item["id"] is None:
                continue
            id_key = str(norm_item["id"])
            entry = {**norm_item, "_source_index": len(normalized_items)}
            normalized_items.append(entry)
        except Exception as e:
            error_entry = {"error": str(e), "original_input": item}
            normalized_items.append(error_entry)
    organized_data = {}
    for idx, entry in enumerate(normalized_items):
        if isinstance(entry.get("id"), int):
            key = f"item_{idx}"
        elif isinstance(entry["id"], str):
            parts = entry["id"].split(":")
            base_type = parts[0] if len(parts) > 1 else "generic"
            value_part = ":".join(parts[1:]) if len(parts) > 1 else ""
            key = f"{base_type}:{value_part}"
        else:
            continue
        organized_data[key] = {**entry, "_order": idx}
    return {"data": organized_data, "total_count": len(organized_data)}
if __name__ == '__main__':
    sample_inputs = [42, 3.14, "hello world", {"key": "value"}, None, True]
    result_dict = process_list(sample_inputs)
    print(result_dict)