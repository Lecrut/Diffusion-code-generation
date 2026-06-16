import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
def process_order(customer_id: str, item_category: str, quantity: int) -> dict:
    logging.debug(f"Processing order for Customer {customer_id} with Category '{item_category}'")
    if not isinstance(customer_id, str):
        return {"status": "error", "message": f"Invalid customer ID: Expected string, got {type(customer_id).__name__}", "action_taken": "rejected"}
    valid_customers = ["C001", "C002"]
    if customer_id not in valid_customers:
        return {"status": "error", "message": f"Customer '{customer_id}' does not exist.", "action_taken": "denied"}
    logging.debug(f"Validating category for Customer {customer_id}")
    if isinstance(item_category, str):
        valid_categories = ["electronics", "clothing", "food"]
        if item_category.lower() in valid_categories:
            logging.info(f"Category '{item_category}' is approved for Customer {customer_id}")
            max_qty_map = {"electronics": 5, "clothing": 10, "food": 2}
            if item_category.lower() == "electronics":
                logging.debug(f"Checking electronics limit for Customer {customer_id}")
                if quantity <= max_qty_map["electronics"]:
                    return {"status": "success", "message": f"Order placed: {quantity} items of Electronics.", "action_taken": "fulfilled"}
                else:
                    return {"status": "error", "message": f"Quantity exceeds limit for electronics. Max allowed is 5.", "action_taken": "rejected"}
            elif item_category.lower() == "clothing":
                logging.debug(f"Checking clothing limit for Customer {customer_id}")
                if quantity <= max_qty_map["clothing"]:
                    return {"status": "success", "message": f"Order placed: {quantity} items of Clothing.", "action_taken": "fulfilled"}
                else:
                    return {"status": "error", "message": f"Quantity exceeds limit for clothing. Max allowed is 10.", "action_taken": "rejected"}
            elif item_category.lower() == "food":
                logging.debug(f"Checking food limit for Customer {customer_id}")
                if quantity <= max_qty_map["food"]:
                    return {"status": "success", "message": f"Order placed: {quantity} items of Food.", "action_taken": "fulfilled"}
                else:
                    return {"status": "error", "message": f"Quantity exceeds limit for food. Max allowed is 2.", "action_taken": "rejected"}
        logging.warning(f"Category '{item_category}' not in approved list.")
    elif isinstance(quantity, int):
        if quantity < 1:
            return {"status": "error", "message": f"Quantity must be at least 1.", "action_taken": "rejected"}
    logging.error(f"Unhandled category '{item_category}' or invalid data structure.")
    if isinstance(item_category, str):
        return {"status": "error", "message": f"Category '{item_category}' is not recognized.", "action_taken": "denied"}
    logging.error("No valid path found in decision tree.")
    if isinstance(quantity, int):
        return {"status": "error", "message": f"Invalid quantity: {quantity}. Must be positive integer.", "action_taken": "rejected"}
    logging.error("Logic execution completed without success.")
if __name__ == '__main__':
    result_1 = process_order(customer_id="C001", item_category="electronics", quantity=3)
    logging.info(f"Result for C001/Electronics/3: {result_1}")
    result_2 = process_order(customer_id="C002", item_category="toys", quantity=5)
    logging.info(f"Result for C002/toys/5: {result_2}")
    result_3 = process_order(customer_id="C001", item_category="food", quantity=3)
    logging.info(f"Result for C001/Food/3: {result_3}")
    result_4 = process_order(customer_id="UNKNOWN", item_category="clothing", quantity=2)
    logging.info(f"Result for UNKNOWN/Clothing/2: {result_4}")