from typing import Dict, Any, Optional

def check_voter_eligibility(attributes: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    age = attributes.get('age')
    citizenship = attributes.get('citizenship')
    registration = attributes.get('registered', False)
    
    if age is None or citizenship is None:
        raise ValueError("Missing required attributes: 'age' and 'citizenship'")
    
    if not isinstance(age, int) or age < 0:
        raise ValueError("'age' must be a non-negative integer")
    
    if citizenship not in ['citizen', 'non_citizen']:
        raise ValueError("'citizenship' must be either 'citizen' or 'non_citizen'")
    
    eligible = False
    reasons = []
    
    if age < 18:
        reasons.append("under age 18")
    elif citizenship != 'citizen':
        reasons.append("not a citizen")
    elif not registration:
        reasons.append("not registered")
    else:
        eligible = True
        
    return {
        "eligible": eligible,
        "reasons": reasons if not eligible else []
    }

if __name__ == '__main__':
    test_cases = [
        {"age": 25, "citizenship": "citizen", "registered": True},
        {"age": 16, "citizenship": "citizen", "registered": True},
        {"age": 22, "citizenship": "non_citizen", "registered": True},
        {"age": 30, "citizenship": "citizen", "registered": False}
    ]
    
    for voter in test_cases:
        result = check_voter_eligibility(voter)
        print(result)