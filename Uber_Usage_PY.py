from Uber_Class_PY import Uber

uber = Uber()

uber.set_drivers(['D32', 'D8712', 'D922', 'D88'])
uber.set_customers(['C11', 'C934', 'C331'])
uber.set_travel_times({('D32', 'C11'): 587,
 ('D32', 'C331'): 1380,
 ('D32', 'C934'): 915,
 ('D8712', 'C11'): 1734,
 ('D8712', 'C331'): 693,
 ('D8712', 'C934'): 974,
 ('D88', 'C11'): 621,
 ('D88', 'C331'): 1230,
 ('D88', 'C934'): 830,
 ('D922', 'C11'): 1462,
 ('D922', 'C331'): 472,
 ('D922', 'C934'): 958})


uber.build_model()

uber.solve_model()

assignments = uber.assignments()

print("Status:", uber.status())
print("Objective Function Value:", uber.objective_function_value())
print("Solution:", uber.solution())
print("Assignments:", uber.assignments())

