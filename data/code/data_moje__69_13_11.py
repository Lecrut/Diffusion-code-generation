FOOTS_PER_MILE = 5280

def _convert(value, factor):
    return value * factor

def m_to_f(miles):
    return _convert(miles, FOOTS_PER_MILE)

if __name__ == '__main__':
    print(m_to_f(1))
    print(m_to_f(3.25))