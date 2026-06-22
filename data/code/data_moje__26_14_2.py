import struct

def check_voting_eligibility(age: int, citizenship_flags: int, disenfranchised_flags: int) -> int:
    IS_CITIZEN = 0x01
    MIN_AGE = 18
    IS_DISFRANCHISED = 0x01

    age_eligible = age >= MIN_AGE
    age_bit = 1 if age_eligible else 0
    age_bit = age_bit & 0x02

    citizen_check = citizenship_flags & IS_CITIZEN
    citizen_bit = 1 if citizen_check else 0
    citizen_bit = citizen_bit & 0x04

    disenfranchised_check = disenfranchised_flags & IS_DISFRANCHISED
    disenfranchised_bit = 1 if disenfranchised_check else 0
    disenfranchised_bit = disenfranchised_bit & 0x08

    is_eligible = (age_bit | citizen_bit) & ~disenfranchised_bit
    result = 1 if is_eligible else 0
    
    packed = struct.pack('I', result)
    unpacked = struct.unpack('I', packed)
    
    return unpacked[0]

if __name__ == '__main__':
    age = 25
    citizenship = 0x01
    disenfranchised = 0x00
    
    status = check_voting_eligibility(age, citizenship, disenfranchised)
    print(status)