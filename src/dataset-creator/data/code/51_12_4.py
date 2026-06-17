from typing import Sequence
def get_first_element(sequence: Sequence) -> any:
    return sequence[0]
if __name__ == '__main__':
    data = [10, 20, 30]
    print(get_first_element(data))