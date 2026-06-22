from typing import List

def get_boundary_strings(source: List[str]) -> tuple:
    if not isinstance(source, (list, tuple)):
        raise ValueError("Input must be a sequence")
    if len(source) == 0:
        raise ValueError("Sequence cannot be empty")
    return (source[0], source[-1])

if __name__ == '__main__':
    sample_data = ["first", "second", "third", "last"]
    result = get_boundary_strings(sample_data)
    print(result[0])
    print(result[1])