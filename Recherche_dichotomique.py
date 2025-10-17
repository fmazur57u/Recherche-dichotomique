from typing import List


# Implémentation de la Recherche Dichotomique
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return sorted_list[mid]
        elif target > sorted_list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(binary_search([1, 2, 3, 4, 5, 6], 3))
print(binary_search([1, 2, 3, 4, 5, 6], 7))
print(binary_search([1, 2, 3, 4, 5, 6], 1))
print(binary_search([1, 2, 3, 4, 5, 6], 6))
print(binary_search(["arbre", "bébé", "caisse", "dinde", "sport", "zoo"], "dinde"))

# Gestion de Cas Spéciaux
print(binary_search([], 1))
# Elle retourne -1

print(binary_search(["chat"], "chat"))
print(binary_search(["chat"], "chien"))

# Les cas particulier marches


# Variation – Première occurrence
def binary_search_first_occurrence(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            if sorted_list[mid - 1] != target or mid == 0:
                return mid
            high = mid - 1
        elif target > sorted_list[mid]:
            low = mid + 1
        else:
            high = mid - 1


print(binary_search_first_occurrence(sorted_list=[1, 2, 2, 2, 3, 4], target=2))
print(
    binary_search_first_occurrence(
        ["arbre", "bébé", "dinde", "dinde", "dinde", "enfer", "zoo"], "dinde"
    )
)
