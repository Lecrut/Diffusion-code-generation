import py_compile
import subprocess

EXECUTE_DEMOS = True
EXEC_TIMEOUT = 5


def compile_source(file_path):
    py_compile.compile(file_path, doraise=True)


def execute_source(file_path, timeout):
    proc = subprocess.run(["python", file_path], capture_output=True, timeout=timeout)
    return proc.returncode, proc.stderr.decode("utf-8", errors="ignore")
