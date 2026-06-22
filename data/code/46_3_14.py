from typing import List, Dict, Any, Optional

def max_salary(records: List[Dict[str, Any]]) -> Optional[float]:
    salaries = map(lambda r: r.get('salary') if isinstance(r.get('salary'), (int, float)) else None, records)
    valid_salaries = [s for s in salaries if s is not None]
    return max(valid_salaries) if valid_salaries else None

if __name__ == '__main__':
    employees = [
        {'name': 'Alice', 'salary': 70000},
        {'name': 'Bob', 'salary': 'unpaid'},
        {'name': 'Charlie', 'salary': 95000.50},
        {'name': 'Diana'}
    ]
    result = max_salary(employees)
    print(result)