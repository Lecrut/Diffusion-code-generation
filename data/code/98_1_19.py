def check_status(age, score, status_code):
    if age < 18:
        return "Minor"
    elif score >= 90:
        return "High Score"
    else:
        if status_code == 200:
            return "Active User"
        else:
            return "Inactive User"

if __name__ == '__main__':
    print(check_status(25, 85, 200))