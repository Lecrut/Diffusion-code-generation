from datetime import datetime
from typing import Any, Dict, Union

def get_voter_eligibility(attributes: Dict[str, Any]) -> str:
    age: Union[int, None] = attributes.get('age')
    citizenship: Union[str, None] = attributes.get('citizenship')
    felony_status: Union[bool, None] = attributes.get('felony_conviction')
    if age is None:
        return 'Invalid: Age missing'
    if citizenship is None:
        return 'Invalid: Citizenship missing'
    try:
        if age < 18:
            return 'Ineligible: Under 18'
        if citizenship.lower() != 'citizen':
            return 'Ineligible: Not a citizen'
        if felony_status:
            return 'Ineligible: Felony conviction'
        return 'Eligible'
    except AttributeError:
        return 'Invalid: Unsupported type'
    except KeyError:
        return 'Invalid: Key error'
if __name__ == '__main__':
    result1: str = get_voter_eligibility({'age': 20, 'citizenship': 'citizen', 'felony_conviction': False})
    print(result1)
    result2: str = get_voter_eligibility({'age': 16, 'citizenship': 'citizen', 'felony_conviction': False})
    print(result2)
    result3: str = get_voter_eligibility({'age': 25, 'citizenship': 'resident', 'felony_conviction': True})
    print(result3)
    result4: str = get_voter_eligibility({'age': 30, 'citizenship': 'citizen', 'felony_conviction': True})
    print(result4)