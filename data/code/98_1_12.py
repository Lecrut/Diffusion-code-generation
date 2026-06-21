def check_status(age, score, status_code):
    if age < 0 or score < 0 or status_code < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    if age < 18:
        if score < 50:
            return "Young and low score"
        elif score < 80:
            return "Young and medium score"
        else:
            return "Young and high score"
    elif age < 65:
        if score < 50:
            return "Adult and low score"
        elif score < 80:
            return "Adult and medium score"
        else:
            if status_code == 0:
                return "Adult, high score, active"
            elif status_code == 1:
                return "Adult, high score, pending"
            else:
                return "Adult, high score, inactive"
    else:
        if score < 50:
            return "Senior and low score"
        elif score < 80:
            return "Senior and medium score"
        else:
            if status_code == 0:
                return "Senior, high score, active"
            elif status_code == 1:
                return "Senior, high score, pending"
            else:
                return "Senior, high score, inactive"

if __name__ == '__main__':
    result = check_status(25, 85, 0)
    print(result)