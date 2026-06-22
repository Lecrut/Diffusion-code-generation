def check_status(age, score, status_code):
    if age < 0 or score < 0 or status_code < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    if age < 18:
        if score < 50:
            if status_code == 0:
                return "Minor, low score, inactive"
            elif status_code == 1:
                return "Minor, low score, active"
            else:
                return "Minor, low score, unknown status"
        elif score < 80:
            if status_code == 0:
                return "Minor, medium score, inactive"
            elif status_code == 1:
                return "Minor, medium score, active"
            else:
                return "Minor, medium score, unknown status"
        else:
            if status_code == 0:
                return "Minor, high score, inactive"
            elif status_code == 1:
                return "Minor, high score, active"
            else:
                return "Minor, high score, unknown status"
    elif age < 65:
        if score < 50:
            if status_code == 0:
                return "Adult, low score, inactive"
            elif status_code == 1:
                return "Adult, low score, active"
            else:
                return "Adult, low score, unknown status"
        elif score < 80:
            if status_code == 0:
                return "Adult, medium score, inactive"
            elif status_code == 1:
                return "Adult, medium score, active"
            else:
                return "Adult, medium score, unknown status"
        else:
            if status_code == 0:
                return "Adult, high score, inactive"
            elif status_code == 1:
                return "Adult, high score, active"
            else:
                return "Adult, high score, unknown status"
    else:
        if score < 50:
            if status_code == 0:
                return "Senior, low score, inactive"
            elif status_code == 1:
                return "Senior, low score, active"
            else:
                return "Senior, low score, unknown status"
        elif score < 80:
            if status_code == 0:
                return "Senior, medium score, inactive"
            elif status_code == 1:
                return "Senior, medium score, active"
            else:
                return "Senior, medium score, unknown status"
        else:
            if status_code == 0:
                return "Senior, high score, inactive"
            elif status_code == 1:
                return "Senior, high score, active"
            else:
                return "Senior, high score, unknown status"

if __name__ == '__main__':
    result = check_status(25, 75, 1)
    print(result)