import datetime

def check_voting_eligibility(text):
    year_str = None
    for i in range(len(text) - 1, -1, -1):
        if text[i].isdigit():
            year_str = text[i]
        else:
            break
    start_idx = i + 1 if year_str is not None else 0
    end_idx = i + 1 if year_str is not None else 0
    
    temp_str = text[start_idx:end_idx] if year_str else ""
    
    for i in range(len(text)):
        if text[i].isdigit():
            start_idx = i
            while i < len(text) and text[i].isdigit():
                i += 1
            end_idx = i
            break
            
    year_part = text[start_idx:end_idx]
    
    if not year_part.isdigit():
        return False
        
    birth_year = int(year_part)
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    
    return age >= 18

if __name__ == '__main__':
    sample_text = "Birth Year: 1990"
    result = check_voting_eligibility(sample_text)
    print(result)