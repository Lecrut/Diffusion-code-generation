import multiprocessing
from typing import List, Union

def _convert_single(number: Union[int, float]) -> str:
    int_part = int(number)
    if int_part == 0:
        return "0"
    result = bin(int_part)[2:]
    return result

def convert_decimals_to_binary(numbers: List[Union[int, float]]) -> List[str]:
    if not numbers:
        return []
    
    with multiprocessing.Pool() as pool:
        results = pool.map(_convert_single, numbers)
    
    return results

if __name__ == "__main__":
    sample_data = [10, 255, 0, 1, 1024, 42, 7, 256, 33]
    binary_results = convert_decimals_to_binary(sample_data)
    print(binary_results)