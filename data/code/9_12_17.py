def trim_spaces(s):
    return s.strip()

if __name__ == '__main__':
    print(trim_spaces('  hello world  '))
    print(trim_spaces('   leading only'))
    print(trim_spaces('trailing only   '))
    print(trim_spaces('no extra spaces'))
    print(trim_spaces('   multiple   spaces   '))
    print(trim_spaces(''))
    print(trim_spaces('   '))