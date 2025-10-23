about_density: list[str] = [
    'Mass per unit of volume describes the density of a substance.',
    'Density is how much matter is contained in a given, specified volume.',
    'A property of all substances is in fact density.',
    '\u03C1 = m / v, the formula that calculates how dense a material is, ',
    'is proportional to mass and inversely proportional to volume.',
    '****************************************************************************************'
    'Atomic mass is responsible for differing densities between different substances.',
    'An object with a greater density than another of the same size will be heavier.',
    'One object can be heavier than another, even if the heavier object is much smaller.',
    'Similarly, an object or even another fluid will sink in another, less dense fluid.',
    'Floating is an example of a less-dense object sitting atop a more dense liquid.',
]
     
if __name__ == '__main__':

    print('**********************************************************************************')

    mass: float = 0
    volume: int = 0
    density: float = 0
    running: bool = False

    try:
        mass = int(input('enter density: '))
        volume = int(input('enter volume: '))
        density = mass / volume

        if volume == 0:
            print('**************************************************************************')
            print(f'{volume} is not possible.')

        if volume < 0:
            volume *= -1
            density *= -1
        running = True

    except ZeroDivisionError:
        print(f'{volume} is an invalid entry.')

    if running:
        print('Your entry:')
        print(f'{mass} / {volume} = {density}')

        print('******************************************************************************')
        for about in about_density:
            print(about)

    else:
        print('******************************************************************************')
        print(f'{mass} / 0 is an invalid fraction\nexiting/')
