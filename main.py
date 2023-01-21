# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting_template= 'Hello, <name>!'):
    return greeting_template.replace('<name>', name)

print(greet('Omari'))
print(greet('Bob', "What's up, <name>!"))

def force(mass, body='earth'):
    surface_gravity = {
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'earth': 9.8,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6,
    }
    gravity = surface_gravity[body]
    return round(mass * gravity, 1)

print(force(10))
print(force(10, body='mars'))

G = 6.674 * (10 ** -11)

def pull(m1, m2, d):
    return G * ((m1 * m2) / (d ** 2))

print(pull(10, 20, 100)) 
