import struct
def sanitize_binary_input(data: bytes) -> bytes:
    return data if isinstance(data, (bytes, bytearray)) else b''
class SafeByteAppender:
    def __init__(self):
        self.buffer = bytearray()
    def append_safe(self, new_data: str | bytes) -> None:
        sanitized = sanitize_binary_input(new_data.encode('utf-8') if isinstance(new_data, str) else new_data)
        try:
            self.buffer.extend(sanitized)
        except MemoryError:
            raise RuntimeError("Buffer allocation failed")
if __name__ == '__main__':
    appender = SafeByteAppender()
    malicious_payload = b'\x00' * 1024 + b'A' * 500
    safe_data = sanitize_binary_input(malicious_payload)
    appender.append_safe(safe_data)
    result = bytes(appender.buffer)
    print(f"Buffer size: {len(result)}")