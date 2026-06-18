import sys
from datetime import datetime
class HierarchicalDecisionEngine:
    def log(self, level: str, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level.upper()}] {message}")
    def process_order(self, customer_id: int, product_category: str, quantity: float) -> dict:
        self.log("INFO", f"Processing order for Customer ID: {customer_id}, Category: {product_category}, Quantity: {quantity}")
        result = {"status": "UNKNOWN", "reason": "", "action_taken": ""}
        if customer_id <= 0:
            self.log("ERROR", f"Invalid customer ID: {customer_id}. Order rejected.")
            return result
        if product_category not in ["electronics", "clothing", "food"]:
            self.log("WARNING", f"Unknown category '{product_category}'. Defaulting to 'other'.")
            product_category = "other"
        if quantity <= 0:
            self.log("ERROR", f"Invalid quantity {quantity}. Order rejected.")
            return result
        if customer_id > 100 and product_category == "electronics":
            if quantity < 2:
                self.log("INFO", f"High value electronics order with low quantity. Applying standard shipping.")
                result["status"] = "SHIPPED_STANDARD"
                result["reason"] = "Standard policy for high-value, single-item orders."
                return result
        elif product_category == "clothing":
            if 5 <= quantity <= 10:
                self.log("INFO", f"Bulk clothing order detected. Applying expedited shipping.")
                result["status"] = "SHIPPED_EXPEDITED"
                result["reason"] = "Bulk discount policy applied."
                return result
        elif product_category == "food":
            if quantity > 50:
                self.log("WARNING", f"Huge food order detected. Manual review initiated.")
                result["status"] = "PENDING_REVIEW"
                result["reason"] = "Threshold exceeded for automated processing."
                return result
        else:
            self.log("INFO", f"No specific tier logic matched. Applying default rules.")
            result["status"] = "SHIPPED_DEFAULT"
            result["reason"] = "Default processing protocol executed."
        return result
if __name__ == '__main__':
    engine = HierarchicalDecisionEngine()
    sample_cases = [
        {"customer_id": 1, "product_category": "electronics", "quantity": 5},
        {"customer_id": 200, "product_category": "clothing", "quantity": 7},
        {"customer_id": -5, "product_category": "food", "quantity": 3.5},
        {"customer_id": 150, "product_category": "unknown_item", "quantity": 99},
    ]
    for case in sample_cases:
        print("-" * 40)
        output = engine.process_order(
            customer_id=case["customer_id"],
            product_category=case["product_category"],
            quantity=case["quantity"]
        )
        print(f"\nFinal Output:")
        for key, value in output.items():
            if isinstance(value, str):
                print(f"  {key}: {value}")