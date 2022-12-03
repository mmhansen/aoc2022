test_input1 = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def parse_p1(st):
    elvs = []
    grps = st.strip().split("\n\n")
    for grp in grps:
        lns = grp.strip().split("\n")
        tmp = list(map(float, lns))
        elvs.append(tmp)
    return elvs

t = parse_p1(test_input1)

def solve_p1(elvs):
    return max(sum(elf) for elf in elvs)

t = solve_p1(t)
print(t)

with open("./inputs/d1.txt", 'r', encoding='utf-8') as f:
    input1 = f.read()


t = parse_p1(input1)
print(t)


t = solve_p1(t)
print('p1', int(t))


def solve_p2(elvs):
    st = sorted([sum(elf) for elf in elvs])
    tmp = sum(st[-3:])
    return int(tmp)

# t = parse_p1(test_input1)

# print(solve_p2(t))


t = parse_p1(input1)

print('p2', solve_p2(t))