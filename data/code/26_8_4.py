import datetime

def check_voting_eligibility(text: str) -> bool:
    current_year = datetime.date.today().year
    birth_year_str = None
    for token in text.split():
        token = token.strip()
        if token.startswith("19") or token.startswith("20"):
            try:
                val = int(token)
                if 1900 <= val <= current_year:
                    birth_year_str = str(val)
                    break
            except ValueError:
                continue
    if birth_year_str is None:
        return False
    birth_year = int(birth_year_str)
    birth_month_day = datetime.date(1900, 1, 1)
    try:
        birth_date = datetime.date(birth_year, 1, 1)
    except ValueError:
        return False
    age = current_year - birth_year
    if (datetime.date(current_year, birth_date.month, birth_date.day) > datetime.date.today()):
        age -= 1
    return age >= 18

if __name__ == '__main__':
    sample_text = "Born in 1995"
    result = check_voting_eligibility(sample_text)
    print(result)