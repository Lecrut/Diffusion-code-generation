def check_status(age, score, status_code):
    if age < 0 or score < 0 or status_code < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    if age < 18:
        if score < 50:
            return "Minor with low score"
        else:
            return "Minor with high score"
    elif age < 65:
        if status_code == 0:
            return "Adult inactive"
        elif status_code == 1:
            if score >= 80:
                return "Adult active with high score"
            else:
                return "Adult active with low score"
        else:
            return "Adult with unknown status"
    else:
        if status_code == 0:
            return "Senior inactive"
        elif status_code == 1:
            if score >= 60:
                return "Senior active with sufficient score"
            else:
                return "Senior active with insufficient score"
        else:
            return "Senior with unknown status"

if __name__ == '__main__':
    result = check_status(25, 85, 1)
    print(result)