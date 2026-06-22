from typing import Dict, Any

def check_voter_eligibility(attributes: Dict[str, Any]) -> bool:
    age: int = attributes.get('age', 0)
    is_citizen: bool = attributes.get('is_citizen', False)
    registered: bool = attributes.get('registered', False)
    
    if age < 0 or not isinstance(age, int):
        return False
    
    if age < 18:
        return False
    
    if not is_citizen:
        return False
    
    if not registered:
        return False
    
    return True

if __name__ == '__main__':
    voter_data: Dict[str, Any] = {
        'age': 25,
        'is_citizen': True,
        'registered': True
    }
    
    result: bool = check_voter_eligibility(voter_data)
    print(result)