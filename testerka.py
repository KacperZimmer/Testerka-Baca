import os
import subprocess

def run_cpp_program(program_path, input_data):
    process = subprocess.Popen([program_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input_data)
    if process.returncode != 0:
        print(f"Error while executing {program_path}: {stderr}")
    return stdout.strip()

def run_tests(program1_path, program2_path, test_cases_dir):
    passed_tests = 0
    failed_tests = 0
    for filename in os.listdir(test_cases_dir):
        if filename.endswith(".in"):
            test_case_path = os.path.join(test_cases_dir, filename)
            with open(test_case_path, 'r') as file:
                input_data = file.read().strip()
            
            program1_result = run_cpp_program(program1_path, input_data)
            program2_result = run_cpp_program(program2_path, input_data)
            
            if program1_result == program2_result:
                print(f"\033[92mTest {filename}: Wyniki są takie same.\033[0m") 
                print(program1_result)
                print('\n')
                print(program2_result)

                passed_tests += 1
            else:
                print(f"\033[91mTest {filename}: Wyniki są różne.\033[0m")

                print('\n')
                print("TUTAJ WYNIK NIEWZORC")
                print(program1_result)
                print('\n')
                print("TUTAJ WYNIK WZORCOWY")
                print(program2_result)    
                print('\n')

                failed_tests += 1

    print(f"Ilość testów: {passed_tests + failed_tests}, Przechodzących: {passed_tests}, Nieprzechodzących: {failed_tests}")

def main():
    program1_path = "./doTestow"
    program2_path = "./skonczony"
    test_cases_dir = "S"

    run_tests(program1_path, program2_path, test_cases_dir)

if __name__ == "__main__":
    main()
