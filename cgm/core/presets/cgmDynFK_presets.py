base =  {'n':
{'airDensity': 1.0,
 'collisionLayerRange': 4.0,
 'gravity': 9.8,
 'gravityDirection': [(0.0, -1.0, 0.0)],
 'maxCollisionIterations': 49,
 'planeBounce': 0.0,
 'planeFriction': 0.10000000149011612,
 'planeNormal': [(0.0, 1.0, 0.0)],
 'planeOrigin': [(0.0, 0.0, 0.0)],
 'planeStickiness': 0.0,
 'subSteps': 12,
 'timingOutput': 0,
 'timeScale':1.0,
 'spaceScale':.01,
 'usePlane': False,
 'windDirection': [(1.0, 0.0, 0.0)],
 'windNoise': 0.0,
 'windSpeed': 0.0},
        'hs':
{'attractionDamp': 0.0,
 'attractionScale': {0: (0.0, 1.0, 1.0), 1: (1.0, 0.20000000298023224, 1.0)},
 'bendAnisotropy': 0.0,
 'bendFollow': 1.0,
 'bendResistance': 1.0,
 'bounce': 0.0,
 'clumpCurl': {0: (0.0, 0.5, 1.0)},
 'clumpFlatness': {0: (0.0, 0.0, 1.0)},
 'clumpInterpolation': 0.0,
 'clumpTwist': 0.0,
 'clumpWidth': 1e-05,
 'clumpWidthScale': {0: (0.0, 1.0, 3.0), 1: (1.0, 0.20000000298023224, 3.0)},
 'collide': True,
 'collideGround': False,
 'collideOverSample': 0,
 'collideStrength': 1.0,
 'collideWidthOffset': 0.0,
 'collisionFlag': 2,
 'collisionLayer': 0.0,
 'compressionResistance': 10.0,
 'curl': 0.0,
 'curlFrequency': 10.0,
 'damp': 0.0,
 'detailNoise': 0.0,
 'diffuseRand': 0.2,
 'displacementScale': {0: (0.0, 1.0, 1.0)},
 'displayQuality': 100.0,
 'drag': 0.1,
 'drawCollideWidth': False,
 'dynamicsWeight': 1.0,
 'extraBendLinks': 0,
 'friction': 0.5,
 'groundHeight': 0.0,
 'hairWidth': 1.2,
 'hairWidthScale': {0: (0.800000011920929, 1.0, 1.0),
                    1: (1.0, 0.20000000298023224, 1.0)},
 'hairsPerClump': 1,
 'interpolationRange': 8.0,
 'iterations': 4,
 'lengthFlex': 0.0,
 'mass': 1.0,
 'maxSelfCollisionIterations': 1,
 'motionDrag': 0.0,
 'noStretch': False,
 'noise': 0.0,
 'noiseFrequency': 0.4,
 'noiseMethod': 0,
 'numCollideNeighbors': 4,
 'repulsion': 0.5,
 'restLengthScale': 1.0,
 'selfCollide': False,
 'selfCollideWidthScale': 1.0,
 'selfCollisionFlag': 2,
 'simulationMethod': 3,
 'solverDisplay': 1,
 'startCurveAttract': 0.0,
 'staticCling': 0.0,
 'stickiness': 0.0,
 'stiffness': 0.15,
 'stiffnessScale': {0: (0.0, 1.0, 1.0)},
 'stretchDamp': 0.10000000149011612,
 'stretchResistance': 105.0,
 'subSegments': 0,
 'tangentialDrag': 0.10000000149011612,
 'thinning': 0.0,
 'turbulenceFrequency': 0.2,
 'turbulenceSpeed': 0.2,
 'turbulenceStrength': 0.0,
 'twistResistance': 0.0,
 'valRand': 0.0}}

wind = {
    'n':
    {
    'airDensity':10.0,
    'windSpeed':900,
     'windDirection':[0,0,-1],
     'windNoise':100},
    'hs':
    {'intensity':1.0,
     'frequency':5.0,
     'speed':.2}}

tree = {'hs': {'attractionScale': {0: (0.0, 1.0, 1.0),
                            1: (0.7043478488922119, 0.0, 1.0),
                            2: (0.260869562625885, 0.2199999988079071, 1.0)},
        'damp': 0.2,
        'hairWidth': 0.01,
        'mass': 1000.0,
        'motionDrag': 0.1,
        'solverDisplay': 0,
        'startCurveAttract': 10.0,
        'stretchResistance': 10.0}}

chain = {'hs': {'attractionScale': {0: (0.0, 1.0, 1.0)},
        'compressionResistance': 1.0526316165924072,
        'damp': 0.001,
        'hairWidth': 50.0,
        'mass': 1000.0,
        'solverDisplay': 0,
        'stretchResistance': 200.0}}

rope = {'hs': {'drag': 0.05,
        'hairWidth': 50.0,
        'mass': 50.0,
        'solverDisplay': 0,
        'stiffnessScale': {0: (0.0, 0.3400000035762787, 1.0)},
        'stretchResistance': 10.0}}

tentacle = {'hs': {'attractionScale': {1: (0.2869565188884735,
                                    0.20000000298023224,
                                    1.0),
                               2: (0.530434787273407, 0.0, 1.0),
                               3: (0.0, 1.0, 1.0)},
           'bendResistance': 0.5,
           'collide': False,
           'damp': 0.02,
           'hairWidth': 5.0,
           'mass': 100.0,
           'startCurveAttract': 1.0,
           'stiffnessScale': {0: (0.0, 1.0, 1.0),
                              1: (0.469565212726593, 1.0, 1.0),
                              2: (0.791304349899292, 0.30000001192092896, 1.0)}}}

limb = {'hs': {'attractionScale': {0: (0.0, 0.6600000262260437, 1.0),
                            1: (1.0, 0.11999999731779099, 1.0),
                            3: (0.373913049697876, 0.5400000214576721, 1.0)},
        'bendResistance': 0.0,
        'compressionResistance': 25.0,
        'damp': 0.1,
        'drag': 0.0,
        'mass': 10.0,
        'startCurveAttract': 0.1,
        'stiffnessScale': {0: (0.0, 0.0, 1.0)},
        'stretchResistance': 25.0,
        'tangentialDrag': 0.0}}
feather = {'hs': {'attractionScale': {1: (1.0, 0.4000000059604645, 3.0),
                            2: (0.0, 0.9200000166893005, 1.0),
                            3: (0.573913037776947, 0.800000011920929, 3.0)},
        'bendResistance': 27.36842155456543,
        'collide': False,
        'compressionResistance': 105.2631607055664,
        'damp': 0.1,
        'drag': 0.0,
        'startCurveAttract': 1.0,
        'stiffnessScale': {0: (0.0, 1.0, 1.0),
                           2: (1.0, 0.5199999809265137, 2.0)},
        'stretchDamp': 0.0,
        'stretchResistance': 200.0,
        'ignoreSolverGravity':1,
        'tangentialDrag': 0.0}}

tail = {'hs': {'attractionScale': {0: (0.0, 1.0, 1.0),
                            1: (0.5043478012084961,
                                 0.03999999910593033,
                                 1.0),
                            2: (0.0, 0.9200000166893005, 1.0),
                            3: (0.27826085686683655,
                                 0.6399999856948853,
                                 1.0)},
        'bendResistance': 27.36842155456543,
        'collide': False,
        'compressionResistance': 105.2631607055664,
        'damp': 0.1,
        'mass': 100.0,
        'startCurveAttract': 0.1,
        'stiffnessScale': {0: (0.0, 1.0, 1.0),
                           1: (0.104347825050354, 0.8799999952316284, 1.0),
                           2: (0.33043476939201355,
                                0.2199999988079071,
                                2.0)},
        'stretchDamp': 0.0,
        'stretchResistance': 200.0}}

dinoTail = {'hs':{'attractionScale': {0: (0.208695650100708, 1.0, 1.0),
                            1: (0.95652174949646, 0.25999999046325684, 1.0),
                            2: (0.017391303554177284, 1.0, 1.0),
                            3: (0.43478259444236755,
                                 0.5799999833106995,
                                 1.0)},
            'bendFollow': False,
            'bendResistance': False,
            'clumpWidth': False,
            'collide': False,
            'collideStrength': False,
            'collisionFlag': False,
            'compressionResistance': False,
            'curlFrequency': False,
            'diffuseRand': False,
            'displayQuality': False,
            'drag': False,
            'dynamicsWeight': False,
            'friction': False,
            'hairWidth': False,
            'hairsPerClump': False,
            'interpolationRange': False,
            'iterations': False,
            'mass': False,
            'maxSelfCollisionIterations': False,
            'noiseFrequency': False,
            'numCollideNeighbors': False,
            'repulsion': False,
            'restLengthScale': False,
            'selfCollideWidthScale': False,
            'selfCollisionFlag': False,
            'simulationMethod': False,
            'solverDisplay': False,
            'stiffness': False,
            'stiffnessScale': {0: (0.0, 1.0, 1.0),
                               1: (0.2956521809101105, 0.9800000190734863, 1.0),
                               3: (0.7652173638343811, 0.2199999988079071, 2.0)},
            'stretchDamp': False,
            'stretchResistance': False,
            'tangentialDrag': False,
            'turbulenceFrequency': False,
            'turbulenceSpeed': False}}

prop = {'hs': {'attractionScale': {0: (0.0, 1.0, 1.0),
                            1: (0.2869565188884735,
                                 0.20000000298023224,
                                 1.0),
                            2: (0.530434787273407, 0.0, 1.0),
                            3: (0.0, 1.0, 1.0)},
        'bendResistance': 0.5,
        'collide': False,
        'damp': 0.01,
        'hairWidth': 5.0,
        'mass': 100.0,
        'startCurveAttract': 0.05,
        'stiffnessScale': {0: (0.0, 1.0, 1.0),
                           1: (0.469565212726593, 1.0, 1.0),
                           2: (0.791304349899292, 0.30000001192092896, 1.0)}}}

cloth = {'hs': {'attractionScale': {0: (0.0, 1.0, 1.0),
                            1: (0.539130449295044, 0.0, 1.0),
                            2: (0.30434781312942505,
                                 0.10000000149011612,
                                 1.0)},
        'bendResistance': 0.10000000149011612,
        'collide': False,
        'compressionResistance': 83.15789794921875,
        'damp': 0.01,
        'extraBendLinks': 1,
        'mass': 5000.0,
        'startCurveAttract': 1.0,
        'stiffnessScale': {0: (0.208695650100708, 0.10000000149011612, 1.0),
                           1: (0.0, 1.0, 1.0),
                           2: (0.52173912525177, 0.0, 1.0)},
        'stretchDamp': 10.0,
        'stretchResistance': 200.0,
        'twistResistance': 0.1}}

spine = {'hs': {'attractionDamp': 0.36813186829561717,
        'attractionScale': {4: (0.0, 1.0, 1.0),
                            5: (0.2869565188884735,
                                 0.20000000298023224,
                                 1.0),
                            6: (0.947826087474823,
                                 0.46000000834465027,
                                 1.0)},
        'bendResistance': 0.0,
        'compressionResistance': 1.0,
        'damp': 0.1,
        'drag': 1.0,
        'mass': 100.0,
        'motionDrag': 0.2,
        'startCurveAttract': 1.0,
        'stiffnessScale': {0: (0.0, 1.0, 1.0),
                           1: (0.0, 1.0, 1.0),
                           2: (0.46086955070495605,
                                0.41999998688697815,
                                1.0),
                           3: (1.0, 0.0, 1.0)},
        'stretchDamp': 100.0,
        'stretchResistance': 100.0,
        'tangentialDrag': 1.0}}
ponytail = {'hs': {'attractionScale': {0: (0.0, 1.0, 1.0),
                            1: (0.5043478012084961,
                                 0.03999999910593033,
                                 1.0),
                            2: (0.0, 0.9200000166893005, 1.0),
                            3: (0.14782609045505524,
                                 0.11999999731779099,
                                 1.0)},
        'bendResistance': 0.10000000149011612,
        'collideGround': True,
        'collideOverSample': 1,
        'drag': 1.0,
        'friction': 0.1,
        'mass': 10.0,
        'motionDrag': 1.0,
        'selfCollide': True,
        'startCurveAttract': 0.1,
        'stiffnessScale': {0: (0.0, 0.30000001192092896, 1.0),
                           1: (0.2869565188884735, 0.0, 1.0)},
        'stretchResistance': 200.0}}

ponytail2 = {'hs': {'attractionScale': {0: (0.0, 1.0, 1.0),
                            1: (0.20000000298023224, 0.0, 1.0),
                            2: (0.0, 0.9200000166893005, 1.0)},
        'bendResistance': 0.0,
        'bounce': 0.25,
        'collideGround': True,
        'collideOverSample': 1,
        'drag': 0.0,
        'extraBendLinks': 1,
        'friction': 0.1,
        'mass': 1000.0,
        'maxSelfCollisionIterations': 2,
        'motionDrag': 0.09,
        'selfCollide': True,
        'simulationMethod': 0,
        'startCurveAttract': 1.0,
        'stiffnessScale': {0: (0.0, 0.10000000149011612, 1.0)},
        'stretchResistance': 200.0,
        'tangentialDrag': 1.0}}

d_chain = {'base':
           {'n':
            {'airDensity': 1.0,
             'collisionLayerRange': 4.0,
             'collisionSoftness': 0.0,
             'currentTime': 1.0,
             'enable': True,
             'frameJumpLimit': 1,
             'gravity': 9.800000190734863,
             'gravityDirection': [(0.0, -1.0, 0.0)],
             'gravityDirectionX': 0.0,
             'gravityDirectionY': -1.0,
             'gravityDirectionZ': 0.0,
             'maxCollisionIterations': 4,
             'planeBounce': 0.0,
             'planeFriction': 0.10000000149011612,
             'planeNormal': [(0.0, 1.0, 0.0)],
             'planeNormalX': 0.0,
             'planeNormalY': 1.0,
             'planeNormalZ': 0.0,
             'planeOrigin': [(0.0, 0.0, 0.0)],
             'planeOriginX': 0.0,
             'planeOriginY': 0.0,
             'planeOriginZ': 0.0,
             'planeStickiness': 0.0,
             'rotateX': 0.0,
             'rotateY': 0.0,
             'rotateZ': 0.0,
             'scaleX': 1.0,
             'scaleY': 1.0,
             'scaleZ': 1.0,
             'spaceScale': 1.0,
             'startFrame': 1.0,
             'subSteps': 3,
             'timeScale': 1.0,
             'translateX': 0.0,
             'translateY': 0.0,
             'translateZ': 0.0,
             'usePlane': False,
             'useTransform': True,
             'visibility': True,
             'windDirection': [(1.0, 0.0, 0.0)],
             'windDirectionX': 1.0,
             'windDirectionY': 0.0,
             'windDirectionZ': 0.0,
             'windNoise': 0.0,
             'windSpeed': 0.0},
           'hs':
           {'attractionDamp': 0.0,
            'baldnessMap': 1.0,
            'bendAnisotropy': 0.0,
            'bendFollow': 1.0,
            'bendResistance': 1.0,
            'bounce': 0.0,
            'castShadows': True,
            'clumpCurl': {0: (0.0, 0.5, 1.0)},
            'clumpFlatness': {0: (0.0, 0.0, 1.0)},
            'clumpInterpolation': 0.0,
            'clumpTwist': 0.0,
            'clumpWidth': 1e-05,
            'clumpWidthScale': {0: (0.0, 1.0, 3.0), 1: (1.0, 0.20000000298023224, 3.0)},
            'collide': True,
            'collideGround': False,
            'collideOverSample': 0,
            'collideStrength': 1.0,
            'collideWidthOffset': 0.0,
            'collisionFlag': 2,
            'collisionLayer': 0.0,
            'compressionResistance': 10.0,
            'curl': 0.0,
            'curlFrequency': 10.0,
            'currentTime': 1.0,
            'damp': 0.0,
            'detailNoise': 0.0,
            'diffuseRand': 0.2,
            'disableFollicleAnim': False,
            'displacementScale': {0: (0.0, 1.0, 1.0)},
            'displayColorB': 0.0,
            'displayColorG': 0.800000011920929,
            'displayColorR': 1.0,
            'displayQuality': 100.0,
            'drag': 0.05,
            'drawCollideWidth': False,
            'dynamicsWeight': 1.0,
            'extraBendLinks': 0,
            'friction': 0.5,
            'gravity': 0.98,
            'groundHeight': 0.0,
            'hairColorB': 0.15000000596046448,
            'hairColorG': 0.25,
            'hairColorR': 0.30000001192092896,
            'hairColorScale': {0: False, 1: False, 2: False},
            'hairWidth': 0.01,
            'hairWidthScale': {0: (0.800000011920929, 1.0, 1.0),
                               1: (1.0, 0.20000000298023224, 1.0)},
            'hairsPerClump': 1,
            'hueRand': 0.0,
            'ignoreSolverGravity': False,
            'ignoreSolverWind': False,
            'interpolationRange': 8.0,
            'iterations': 4,
            'lengthFlex': 0.0,
            'lightEachHair': False,
            'mass': 1.0,
            'maxSelfCollisionIterations': 1,
            'motionDrag': 0.0,
            'multiStreakSpread1': 0.3,
            'multiStreakSpread2': 0.1,
            'multiStreaks': 0,
            'noStretch': False,
            'noise': 0.0,
            'noiseFrequency': 0.4,
            'noiseFrequencyU': 1.0,
            'noiseFrequencyV': 1.0,
            'noiseFrequencyW': 1.0,
            'noiseMethod': 0,
            'numCollideNeighbors': 4,
            'numUClumps': 15.0,
            'numVClumps': 15.0,
            'opacity': 1.0,
            'playFromCache': False,
            'repulsion': 0.5,
            'restLengthScale': 1.0,
            'satRand': 0.0,
            'selfCollide': False,
            'selfCollideWidthScale': 1.0,
            'selfCollisionFlag': 2,
            'simulationMethod': 3,
            'specularColorB': 0.30000001192092896,
            'specularColorG': 0.3499999940395355,
            'specularColorR': 0.3499999940395355,
            'specularPower': 3.0,
            'specularRand': 0.4,
            'startCurveAttract': 0.0,
            'startFrame': 1.0,
            'staticCling': 0.0,
            'stickiness': 0.0,
            'stiffness': 0.15,
            'stiffnessScale': {0: (0.0, 1.0, 1.0)},
            'stretchDamp': 0.10000000149011612,
            'stretchResistance': 10.0,
            'subClumpMethod': 0,
            'subClumpRand': 0.0,
            'subClumping': 0.0,
            'subSegments': 0,
            'tangentialDrag': 0.10000000149011612,
            'thinning': 0.0,
            'translucence': 0.5,
            'turbulenceFrequency': 0.2,
            'turbulenceSpeed': 0.2,
            'turbulenceStrength': 0.0,
            'twistResistance': 0.0,
            'usePre70ForceIntensity': False,
            'valRand': 0.0,
            'widthDrawSkip': 2}},
           
           'default':
           {'n':
            {'subSteps':12,
            'maxCollisionIterations':49,
            'gravity':98,
            'gravityDirection':[0,-1,0]},
            'hs':
            {'bendFollow':1.0,
             'hairWidth':1.2,
             'solverDisplay':1,
             'stretchResistance':105,
             'drag':.1,
             'tangentalDrag':.1,
             }
            },
           'wind':
           {'n':
            {'windSpeed':900,
                        'windDirection':[0,0,-1],
                        'windNoise':5},
            'hs':{'intensity':1.0,
                  'frequency':5.0,
                  'speed':.2}}}