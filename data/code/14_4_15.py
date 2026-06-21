from typing import Sequence

THIRD_INDEX = 2
VALIDATION_THRESHOLD = 2
SAMPLE_DATA = ("zero", "one", "two", "three", "four")

def _validate_third_access(source: Sequence) -> None:
    if len(source) < VALIDATION_THRESHOLD:
        raise ValueError("Data source is insufficient for access.")

def retrieve_third_element(data: Sequence) -> str:
    _validate_third_access(data)
    return str(data[THIRD_INDEX])

if __name__ == '__main__':
    output = retrieve_third_element(SAMPLE_DATA)
    print(output)