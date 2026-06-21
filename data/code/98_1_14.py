def check_status(age, score, status_code):
    if age < 0 or score < 0 or status_code < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    if age < 18:
        if score < 50:
            return "Young and low score"
        else:
            return "Young and high score"
    elif age < 65:
        if score < 50:
            return "Adult and low score"
        else:
            if status_code == 0:
                return "Adult, high score, inactive"
            elif status_code == 1:
                return "Adult, high score, active"
            else:
                return "Adult, high score, unknown status"
    else:
        if score < 50:
            return "Senior and low score"
        else:
            if status_code == 0:
                return "Senior, high score, inactive"
            elif status_code == 1:
                return "Senior, high score, active"
            else:
                return "Senior, high score, unknown status"

if __name__ == '__main__':
    result = check_status(25, 80, 1)
    print(result)