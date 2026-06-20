class AccessControl:
    MIN_AGE = 18

    @staticmethod
    def is_eligible(age, permission):
        return age >= AccessControl.MIN_AGE or permission == 'yes'

if __name__ == '__main__':
    print(AccessControl.is_eligible(20, 'no'))
    print(AccessControl.is_eligible(15, 'yes'))