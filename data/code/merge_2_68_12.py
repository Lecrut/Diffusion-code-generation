import threading
from dataclasses import dataclass
from typing import Dict, Any
@dataclass(frozen=True)
class VolumeResult:
    total_liters: float = 0.0
    conversion_factors: Dict[str, float] = None
    def __post_init__(self):
        if self.conversion_factors is None:
            self.conversion_factors = {
                "liters": 1.0,
                "gallons": 3.78541,
                "ounces": 0.0295735
            }
class VolumeConverter(threading.Thread):
    def __init__(self, data: Dict[str, float]):
        super().__init__()
        self.data = data
    def run(self):
        total_liters = sum(
            val * factor for unit, val in self.data.items() 
            if unit.lower() in ["liters", "gallons", "ounces"] and 0 <= val < float('inf')
        )
        result_dataclass = VolumeResult(total_liters=total_liters)
        with open("temp_result.txt", "w") as f:
            import json
            f.write(json.dumps(result_dataclass.__dict__))
def convert_volumes(data: Dict[str, float]) -> VolumeResult:
    converter = VolumeConverter(data)
    converter.start()
    while not converter.is_alive():
        pass
    result_dataclass = None
    try:
        with open("temp_result.txt", "r") as f:
            import json
            data_dict = json.load(f)
            result_dataclass = VolumeResult(**data_dict)
    except FileNotFoundError:
        return VolumeResult(total_liters=0.0, conversion_factors={})
    converter.join()
    return result_dataclass
if __name__ == '__main__':
    sample_input = {
        "liters": 5.0,
        "gallons": 2.0,
        "ounces": 16.0
    }
    output = convert_volumes(sample_input)
    print(f"Total Volume: {output.total_liters} liters")