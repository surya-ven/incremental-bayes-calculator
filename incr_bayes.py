def get_query():
    p_H = input("Enter P(H): ")
    p_M_H = input("Enter P(M|H): ")
    p_nM_nH = input("Enter P(-M|-H): ")
    return float(p_H), float(p_M_H), float(p_nM_nH)

# Get measurement list
# 0: first measurement, 1: pos, -1: neg
def get_Ms():
    Ms = ["0"]
    i = 1
    while True:
        M = input(f"Enter M for T = {i}: ")
        if M == "":
            break
        Ms.append(M)
        i += 1
    return Ms

def incr_bayes_table():
    p_H, p_M_H, p_nM_nH = get_query()
    p_nM_H, p_M_nH = 1 - p_M_H, 1 - p_nM_nH
    Ms = get_Ms()
    posterior_list = [p_H]
    for M in Ms:
        new_H = posterior_list[-1]
        if M == "0":
            continue
        elif M == "1":
            new_H = p_M_H * new_H / (p_M_H * new_H + p_M_nH * (1 - new_H))
        elif M == "-1":
            new_H = p_nM_H * new_H / (p_nM_H * new_H + p_nM_nH * (1 - new_H))
        else:
            print("Error: M is not 0, 1, or -1")
            exit(1)
        posterior_list.append(new_H)
    return Ms, posterior_list

def display_table(Ms, posterior_list):
    print("\n*********** START *********")
    for i in range(len(Ms)):
        print("Time", i, "M =", Ms[i], "P(H) =", round(posterior_list[i], 4), "P(-H) =", round(1 - posterior_list[i], 4), sep="\t")
    print("***********  END  *********")

Ms, posterior_list = incr_bayes_table()
display_table(Ms, posterior_list)