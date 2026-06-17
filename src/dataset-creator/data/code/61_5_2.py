def convert_seconds_to_hm(total_seconds: int) -> tuple[int, int]:
    return divmod(total_seconds, 3600), divmod(divmod(total_seconds, 3600)[1], 60)
if __name__ == '__main__':
    sample_total = 7254
    h_m_s = convert_seconds_to_hm(sample_total)
    print(f"{h_m_s[0]} hours and {h_m_s[1][0]} minutes")