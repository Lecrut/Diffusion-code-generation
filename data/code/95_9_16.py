from typing import List

THRESHOLD: int = 100
LABEL_POSITIVE: str = "positive"
LABEL_EVEN: str = "even"
LABEL_THRESHOLD: str = f"less than {THRESHOLD}"
SEPARATOR: str = " and "
DEFAULT_LABEL: str = "none"

def combine_checks(is_positive: bool, is_even: bool, is_less_than_100: bool) -> str:
    matching_labels: List[str] = []
    
    if is_positive:
        matching_labels.append(LABEL_POSITIVE)
    
    if is_even:
        matching_labels.append(LABEL_EVEN)
        
    if is_less_than_100:
        matching_labels.append(LABEL_THRESHOLD)
        
    if not matching_labels:
        return DEFAULT_LABEL
        
    return SEPARATOR.join(matching_labels)

if __name__ == '__main__':
    print(combine_checks(True, True, True))
    print(combine_checks(False, False, False))
    print(combine_checks(True, False, True))
    print(combine_checks(False, True, True))
    print(combine_checks(True, True, False))
    print(combine_checks(False, True, False))
    print(combine_checks(False, False, True))
    print(combine_checks(True, False, False))