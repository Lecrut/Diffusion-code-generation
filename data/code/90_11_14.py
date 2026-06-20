def check_access(age, permission):
    access_rules = {
        'adult': age >= 18,
        'granted': permission == 'yes'
    }
    return access_rules['adult'] or access_rules['granted']

if __name__ == '__main__':
    print(check_access(20, 'no'))
    print(check_access(15, 'yes'))