PASS_THRESHOLD = 60

def check_status(score):
    return 'Pass' if score >= PASS_THRESHOLD else 'Fail'

if __name__ == '__main__':
    print(check_status(55))
    print(check_status(70))