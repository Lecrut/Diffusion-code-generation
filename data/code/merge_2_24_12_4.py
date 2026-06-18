import time
def build_item_list(items: list) -> dict:
    start_time = time.time()
    processed_items = []
    for idx, item in enumerate(items):
        if isinstance(item, (dict, str)):
            entry = {
                "id": f"item_{idx}",
                "data": item,
                "processed_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "status": "validated"
            }
        else:
            raise ValueError(f"Unsupported item type at index {idx}: {type(item)}")
        processed_items.append(entry)
    end_time = time.time()
    return {
        "total_count": len(processed_items),
        "processing_duration_ms": round((end_time - start_time) * 1000, 2),
        "items": processed_items
    }
if __name__ == '__main__':
    sample_data = [
        {"type": "product", "code": "ABC-123"},
        "Simple string item",
        ["nested_list_item_1"],
        456,
        None
    ]
    try:
        result = build_item_list(sample_data)
        print(f"Total items processed: {result['total_count']}")
        print(f"Processing time: {result['processing_duration_ms']} ms")
        for item in result["items"]:
            if isinstance(item, dict):
                print(f"[{item['id']}] Status: {item['status']} | Data Type: {type(item.get('data')).__name__}")
    except ValueError as e:
        print(f"Error during processing: {e}")