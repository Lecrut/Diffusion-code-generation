def trim_string(s):
    return s.strip()

if __name__ == '__main__':
    print(trim_string('  hello world  '))
    print(trim_string('no_spaces'))
    print(trim_string('   '))
    print(trim_string('  mixed   spaces  '))