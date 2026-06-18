from typing import Dict, Any
class DynamicSelector:
    def __init__(self) -> None:
        self.choices: Dict[int, str] = {1: "Option A", 2: "Option B"}
        self.selected_choice: int | None = None
    def process_selection(self, choice_index: int) -> Any:
        if not (1 <= choice_index <= len(self.choices)):
            raise ValueError("Invalid choice. Must be between 1 and number of options.")
        self.selected_choice = choice_index
        if choice_index == 1:
            return {"status": "success", "message": f"Executing Option A logic."}
        elif choice_index == 2:
            return {"status": "warning", "message": f"Running Option B process with caution."}
        else:
            raise RuntimeError("Unexpected selection error.")
if __name__ == '__main__':
    selector = DynamicSelector()
    SAMPLE_INPUTS = [1, 2]
    for choice in SAMPLE_INPUTS:
        try:
            result = selector.process_selection(choice)
            print(f"Choice {choice}: {result}")
        except (ValueError, RuntimeError) as e:
            print(f"Error handling choice {choice}: {e}")