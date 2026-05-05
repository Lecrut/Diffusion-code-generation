import sys
def time_to_minutes(time_str):
    h_str, m_str, s_str = time_str.split(':')
    h = int(h_str)
    m = int(m_str)
    s = int(s_str)
    total_minutes = h * 60 + m + s
    return total_minutes
if __name__ == '__main__':
    sample_time = "01:30:45"
    result = time_to_minutes(sample_time)
    print(result)