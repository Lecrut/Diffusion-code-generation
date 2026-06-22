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
            if status_code == 0:
                return "Adult and medium score, active"
            elif status_code == 1:
                return "Adult and medium score, pending"
            else:
                return "Adult and medium score, inactive"
        else:
            return "Adult and high score"
    else:
        if score < 50:
            return "Senior and low score"
        elif score < 80:
            return "Senior and medium score"
        else:
            if status_code == 0:
                return "Senior and high score, active"
            elif status_code == 1:
                return "Senior and high score, pending"
            else:
                return "Senior and high score, inactive"

if __name__ == '__main__':
    result = check_status(25, 75, 1)
    print(result)