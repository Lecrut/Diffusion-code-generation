class TimeConverter:
    def convert_to_total_minutes(self, time_str):
        h_str, m_str, s_str = time_str.split(':')
        h = int(h_str)
        m = int(m_str)
        s = int(s_str)
        total_minutes = h * 60 + m + s / 60
        return total_minutes

if __name__ == '__main__':
    converter = TimeConverter()
    print(converter.convert_to_total_minutes('1:30:45'))