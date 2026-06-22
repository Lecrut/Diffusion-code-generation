def process_items(items):
    results = []
    for item in items:
        status = item.get("status", "")
        is_premium = item.get("is_premium", False)
        price = item.get("price", 0)
        
        if status == "active" and is_premium:
            final_price = price * 0.8
            results.append({"id": item.get("id"), "final_price": final_price, "note": "Premium active discount"})
        elif status == "active":
            final_price = price
            results.append({"id": item.get("id"), "final_price": final_price, "note": "Standard active"})
        elif status == "expired":
            results.append({"id": item.get("id"), "final_price": 0, "note": "Expired item"})
        else:
            raise ValueError(f"Unsupported status: {status}")
            
    return results

if __name__ == '__main__':
    sample_items = [
        {"id": 1, "status": "active", "is_premium": True, "price": 100},
        {"id": 2, "status": "active", "is_premium": False, "price": 50},
        {"id": 3, "status": "expired", "is_premium": True, "price": 200},
        {"id": 4, "status": "inactive", "is_premium": False, "price": 10}
    ]
    
    try:
        output = process_items(sample_items)
        print(output)
    except ValueError as e:
        print(f"Error: {e}")