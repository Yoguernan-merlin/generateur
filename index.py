def generate_primes(n):
    # Si n est inférieur à 2, il n'y a pas de nombres premiers
    if n < 2:
        return []
    
    # Initialisation d'une liste pour stocker les nombres premiers
    primes = []
    # Parcourt tous les nombres de 2 à n
    for num in range(2, n + 1):
        is_prime = True
        # Supposons que num est premier
        # Vérifie si num est divisible par un nombre entre 2 et √num
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False  # num n'est pas premier
                break  # Sortir de la boucle, inutile de vérifier les autres divisors
            # Si num est toujours considéré comme premier, on l'ajoute à la liste

        if is_prime:# Retourne la liste des nombres premiers
            primes.append(num)
    
    return primes

# Exemple d'utilisation
n = 350
print(f"Nombres premiers inférieurs ou égaux à {n} : {generate_primes(n)}")
