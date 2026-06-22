from typing import List, Any, Optional

def max_salary(records: List[List[Any]]) -> Optional[float]:
    salaries = list(map(lambda r: float(r[2]) if isinstance(r[2], (int, float)) else None, records))
    valid_salaries = list(filter(lambda s: s is not None, salaries))
    return max(valid_salaries) if valid_salaries else None

if __name__ == '__main__':
    data = [['Alice', 25, 50000], ['Bob', 30, 75000.5], ['Charlie', 35, 'invalid']]
    print(max_salary(data))