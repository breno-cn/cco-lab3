from typing import List


def jordan(mat: List[List[float]]) -> List[float]:
    num_coeficientes = len(mat)
    tam_extendido = len(mat[0])

    for i in range(num_coeficientes):
        pivot = mat[i][i]

        for j in range(num_coeficientes):
            if j != i:
                termo = mat[j][i]
                coeficiente = termo / pivot

                for k in range(tam_extendido):
                    mat[j][k] = mat[j][k] - (mat[i][k] * coeficiente)

    res = []
    for i in range(num_coeficientes):
        res.append(mat[i][tam_extendido - 1] / mat[i][i])

    for line in mat:
        print(line)

    return res

mat = [
    [2, 4, -5, 5],
    [4, 1, -5, 2],
    [2, 4, 5, 1]
]

print(mat)

res = jordan(mat)

for line in res:
    print(line)
