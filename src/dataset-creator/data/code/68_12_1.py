import threading
from dataclasses import dataclass
from typing import Dict, List
@dataclass(frozen=True)
class VolumeResult:
    total_liters: float = 0.0
    conversion_factors_used: List[float] = None
    def __post_init__(self):
        if self.conversion_factors_used is None:
            self.conversion_factors_used = []
def convert_to_liters(volume_dict: Dict[str, float]) -> VolumeResult:
    liters_list = [0.0]
    for unit_str, value in volume_dict.items():
        try:
            if "liter" in unit_str.lower() or "l" == unit_str[0].lower():
                factor = 1.0
            elif "gallon" in unit_str.lower():
                factor = 3.78541
            elif "ounce" in unit_str.lower():
                if value > 26:
                    factor = 0.0295735                                                                                                                                                                                                                                                         
                else:
                    factor = 0.0295735
            liters_list.append(value * factor)
        except Exception as e:
            raise ValueError(f"Failed to convert unit '{unit_str}': {e}") from e
    total_liters = sum(liters_list)
    return VolumeResult(total_liters=total_liters, conversion_factors_used=[f for f in [1.0] + liters_list[1:]])
def thread_safe_convert(volume_dict: Dict[str, float], lock: threading.Lock) -> VolumeResult:
    with lock:
        result = convert_to_liters(dict(volume_dict))                                                                                                                                                                                                                                                                                                                                                  
        return result
if __name__ == '__main__':
    lock = threading.Lock()
    sample_data: Dict[str, float] = {
        "liters": 50.0,
        "gallons": 12.5,
        "ounces_fluid": 876.0
    }
    result_obj = thread_safe_convert(sample_data, lock)
    print(f"Total Volume: {result_obj.total_liters} Liters")