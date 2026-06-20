def check_status(age, score, status_code):
    if age < 18:
        return "Minor"
    elif age >= 65:
        return "Senior"
    else:
        if score < 50:
            return "Low Score"
        elif score >= 90:
            return "High Score"
        else:
            if status_code == 200:
                return "Active User"
            elif status_code == 404:
                return "Inactive User"
            else:
                return "Unknown Status"

if __name__ == '__main__':
    print(check_status(17, 45, 200))
    print(check_status(66, 95, 404))
    print(check_status(30, 85, 200))
    print(check_status(25, 45, 404))