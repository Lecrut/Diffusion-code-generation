def time_to_seconds(time_str: str) -> int:
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def time_diff_in_ms(time_str1: str, time_str2: str) -> int:
    return abs(time_to_seconds(time_str2) - time_to_seconds(time_str1)) * 1000

if __name__ == '__main__':
    print(time_diff_in_ms("12:34:56", "12:34:57"))