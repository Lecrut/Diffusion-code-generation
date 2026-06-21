import datetime

def check_voting_eligibility(birth_string: str) -> dict:
    try:
        year_part = birth_string.split('-')[2]
        birth_year = int(year_part)
    except (IndexError, ValueError):
        return {
            "eligible": False,
            "message": "Invalid birth year format"
        }

    current_year = datetime.datetime.now().year
    age = current_year - birth_year

    if age < 0:
        return {
            "eligible": False,
            "message": "Future birth year detected"
        }

    eligible = age >= 18

    return {
        "eligible": eligible,
        "age": age,
        "birth_year": birth_year
    }

if __name__ == '__main__':
    result = check_voting_eligibility("1990-05-15")
    print(result)
    result2 = check_voting_eligibility("2010-01-01")
    print(result2)
    result3 = check_voting_eligibility("abc-def-ghi")
    print(result3)