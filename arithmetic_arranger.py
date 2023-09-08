def arithmetic_arranger(problems, show_results=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    top_line = []
    bottom_line = []
    dash_line = []
    result_line = []

    for problem in problems:
        num1, operator, num2 = problem.split()

        # Check if the operands are numeric
        if not (num1.isnumeric() and num2.isnumeric()):
            return "Error: Numbers must only contain digits."

        # Check if the operator is valid
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-."

        width = max(len(num1), len(num2)) + 2
        top_line.append(num1.rjust(width))
        bottom_line.append(operator + num2.rjust(width - 1))
        dash_line.append("-" * width)

        if show_results:
            if operator == "+":
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            result_line.append(result.rjust(width))

    arranged_problems.append("    ".join(top_line))
    arranged_problems.append("    ".join(bottom_line))
    arranged_problems.append("    ".join(dash_line))

    if show_results:
        arranged_problems.append("    ".join(result_line))

    return "\n".join(arranged_problems)
