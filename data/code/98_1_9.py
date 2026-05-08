def check_status(age, score, status_code):
    if age < 18:
        if score >= 90:
            if status_code == 200:
                return "Minor with high score and OK status"
            elif status_code == 404:
                return "Minor with high score and Not Found status"
            else:
                return "Minor with high score and other status"
        elif score >= 70:
            if status_code == 200:
                return "Young adult with good score and OK status"
            else:
                return "Young adult with good score and other status"
        else:
            return "Minor with low score and other status"
    elif 18 <= age < 65:
        if score >= 90:
            if status_code == 200:
                return "Adult with high score and OK status"
            else:
                return "Adult with high score and other status"
        else:
            if status_code == 200:
                return "Adult with good score and OK status"
            else:
                return "Adult with good score and other status"
    else:
        if status_code == 200:
            return "Senior with OK status"
        else:
            return "Other status for senior"
if __name__ == '__main__':
    print(check_status(16, 95, 200))
    print(check_status(25, 85, 200))
    print(check_status(30, 92, 404))
    print(check_status(50, 75, 200))
    print(check_status(70, 99, 200))
    print(check_status(80, 60, 200))
    print(check_status(85, 90, 200))
    print(check_status(85, 90, 500))