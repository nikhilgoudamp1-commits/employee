def get_employee_details(name, emp_id, department, salary):
    return (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )

# Sample function call (optional)
if __name__ == "__main__":
    result = get_employee_details("John Doe", 101, "HR", 50000)
    print(result)
