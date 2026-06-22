def get_voter_eligibility(attributes: dict) -> str:
    age: int = attributes.get('age', 0)
    citizenship: str = attributes.get('citizenship', '')
    registered: bool = attributes.get('registered', False)

    if age < 18:
        return 'ineligible'
    if citizenship != 'citizen':
        return 'ineligible'
    if not registered:
        return 'ineligible'
    return 'eligible'

if __name__ == '__main__':
    voter_data: dict = {
        'age': 25,
        'citizenship': 'citizen',
        'registered': True
    }
    
    status: str = get_voter_eligibility(voter_data)
    print(status)