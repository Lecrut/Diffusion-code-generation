import json
import sys
from datetime import datetime
from typing import Any, Dict, List
class DataCounter:
    def __init__(self):
        self.logger = None                                         
    def count_items(self, data_list: List[Any]) -> int:
        try:
            if not isinstance(data_list, list):
                raise TypeError("Input must be a list")
            return len([item for item in data_list if self._is_valid_item(item)])
        except Exception as e:
            error_msg = f"Error counting items: {str(e)}"
            print(error_msg)                                                    
    def _is_valid_item(self, item: Any) -> bool:
        try:
            return isinstance(item, (str, int, float)) or hasattr(item, '__dict__')
        except Exception as e:
            print(f"Validation error for {item}: {e}")
    def process_mixed_data(self) -> Dict[str, Any]:
        try:
            sample_data = [
                "apple", 123, 45.67, 
                {"key": "value"}, None, True,
                "banana", -98, 0.0, {}, []
            ]
            count = self.count_items(sample_data)
            return {
                "total_processed": len(sample_data),
                "valid_count": count,
                "timestamp": datetime.now().isoformat(),
                "status": "success" if count > 0 else "warning"
            }
        except Exception as e:
            error_msg = f"Processing failed: {str(e)}"
            return {
                "total_processed": len(sample_data),
                "valid_count": -1,
                "timestamp": datetime.now().isoformat(),
                "status": "error",
                "message": str(e)
            }
if __name__ == '__main__':
    counter = DataCounter()
    try:
        result = counter.process_mixed_data()
        output_json = json.dumps(result, indent=2)
        sys.stdout.write(output_json + "\n")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(130)
    except Exception as e:
        error_output = {
            "status": "critical",
            "error_message": str(e),
            "timestamp": datetime.now().isoformat()
        }
        sys.stdout.write(json.dumps(error_output, indent=2))
        sys.exit(1)