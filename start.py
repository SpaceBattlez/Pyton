import json
import sys

from bot import GameUpdate
from gameElements import GameState

print("Ready!")
sys.stdout.flush()

while True:
    input = sys.stdin.readline()
    input = '{"bots":[{"id":1,"name":"UserBot"},{"id":2,"name":"BasicBot"}],"planets":[{"id":0,"ownerID":2,"position":{"x":451,"y":467},"numberOfShips":29,"growthRate":4},{"id":1,"ownerID":1,"position":{"x":49,"y":33},"numberOfShips":5,"growthRate":4},{"id":2,"ownerID":2,"position":{"x":214,"y":135},"numberOfShips":25,"growthRate":1},{"id":3,"ownerID":1,"position":{"x":286,"y":365},"numberOfShips":2,"growthRate":1},{"id":4,"ownerID":0,"position":{"x":154,"y":147},"numberOfShips":6,"growthRate":2},{"id":5,"ownerID":0,"position":{"x":346,"y":353},"numberOfShips":6,"growthRate":2},{"id":6,"ownerID":0,"position":{"x":303,"y":171},"numberOfShips":13,"growthRate":1},{"id":7,"ownerID":0,"position":{"x":197,"y":329},"numberOfShips":13,"growthRate":1},{"id":8,"ownerID":0,"position":{"x":445,"y":218},"numberOfShips":99,"growthRate":4},{"id":9,"ownerID":0,"position":{"x":55,"y":282},"numberOfShips":99,"growthRate":4},{"id":10,"ownerID":0,"position":{"x":38,"y":384},"numberOfShips":16,"growthRate":4},{"id":11,"ownerID":0,"position":{"x":462,"y":116},"numberOfShips":16,"growthRate":4}],"fleets":[{"id":0,"ownerID":1,"numberOfShips":37,"ticksToDestination":5,"destinationPlanetID":4,"sourcePlanetID":1,"position":{"x":88,"y":75}},{"id":1,"ownerID":1,"numberOfShips":42,"ticksToDestination":1,"destinationPlanetID":5,"sourcePlanetID":3,"position":{"x":331,"y":356}},{"id":2,"ownerID":2,"numberOfShips":7,"ticksToDestination":5,"destinationPlanetID":5,"sourcePlanetID":0,"position":{"x":411,"y":424}},{"id":3,"ownerID":2,"numberOfShips":7,"ticksToDestination":1,"destinationPlanetID":4,"sourcePlanetID":2,"position":{"x":169,"y":144}},{"id":4,"ownerID":1,"numberOfShips":4,"ticksToDestination":6,"destinationPlanetID":4,"sourcePlanetID":1,"position":{"x":75,"y":61}},{"id":5,"ownerID":1,"numberOfShips":1,"ticksToDestination":2,"destinationPlanetID":5,"sourcePlanetID":3,"position":{"x":316,"y":359}},{"id":6,"ownerID":2,"numberOfShips":7,"ticksToDestination":6,"destinationPlanetID":5,"sourcePlanetID":0,"position":{"x":424,"y":438}},{"id":7,"ownerID":2,"numberOfShips":7,"ticksToDestination":2,"destinationPlanetID":4,"sourcePlanetID":2,"position":{"x":184,"y":141}},{"id":8,"ownerID":1,"numberOfShips":4,"ticksToDestination":7,"destinationPlanetID":4,"sourcePlanetID":1,"position":{"x":62,"y":47}},{"id":9,"ownerID":1,"numberOfShips":1,"ticksToDestination":3,"destinationPlanetID":5,"sourcePlanetID":3,"position":{"x":301,"y":362}},{"id":10,"ownerID":2,"numberOfShips":7,"ticksToDestination":7,"destinationPlanetID":5,"sourcePlanetID":0,"position":{"x":437,"y":452}},{"id":11,"ownerID":2,"numberOfShips":7,"ticksToDestination":3,"destinationPlanetID":4,"sourcePlanetID":2,"position":{"x":199,"y":138}}]}'
    state = json.loads(input)

    fleets = GameUpdate(GameState(state["bots"], state["planets"], state["fleets"]))
    
    output = []
    for fleet in fleets:
        output.append(fleet.toJSON())
    
    print('[' + ', '.join(output) + ']')
    sys.stdout.flush()
