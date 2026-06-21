from typing import List, Dict

def count_elements(elements: List) -> Dict:
    counts = {}
    for element in elements:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    return counts
if __name__ == '__main__':
    sample_list = ['cat', 'dog', 'bird', 'fish', 'dog', 'cat']
    result = count_elements(sample_list)
    print(result)