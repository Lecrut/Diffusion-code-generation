def check_status(score):
    if score >= 60:
        return 'Pass'
    else:
        return 'Fail'
if __name__ == '__main__':
    print(check_status(55))
    print(check_status(70))