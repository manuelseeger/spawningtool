"""
spawningtool.coop_constants
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Co-op uses Blizzard time like HotS (16 FPS), so it's easier to base the data off of that.

Co-op also uses the LotV launch chronoboost that stays continuously on one building
"""

from spawningtool.hots_constants import *

BO_EXCLUDED = BO_EXCLUDED.copy()

BO_EXCLUDED.update([
    'Scarab',
    # Raynor
    'HyperionAdvancedPointDefenseDrone',
    'HyperionVoidCoop',  # summoned
    'DuskWing',  # summoned
    'SpiderMine',
    # Kerrigan
    'KerriganReviveCocoon',
    'KerriganVoidCoopEconDrop1',
    'KerriganVoidCoopEconDrop2',
    'KerriganVoidCoopEconDrop3',
    'KerriganVoidCoopEconDrop4',
    'KerriganVoidCoopEconDrop5',
    'KerriganVoidCoopEconDropLT1',
    'NydusNetworkAlly',
    'NydusCanalAlly',
    'GreaterNydusWormAlly',
    # Artanis
    'SOAPylonPowerAllyUnit',
    'SOAPylonPowerUnit',
    # Swann
    'VoidCoopARES',  # Calldown
    # Zagara
    'ZagaraReviveCocoon',
    'HunterKillerBurrowed',  # from Spawn Hunter Killers ability
    'HotSSplitterlingBig',  # Splitter probably from auto-spawn
    'HotSSplitterlingMedium',  # Splitter Baneling Spawn
    # Vorazun
    'VorazunShadowGuard',  # calldown
    # Karax
    'CarrierRepairDrone',
    'SOAThermalLanceTargeter',
    'SOAPurifierBeamUnit',
    # Abathur
    'BiomassPickup',
    'ToxicNest',
    'LocustFlying',
    'BrutaliskPlacement',  # Deep Tunnel
    'AbathurSymbioteBrutalisk',  # paired with building Brutalisk
    'AbathurSymbioteLeviathan',  # paired with building Leviathan

    # Alarak
    'AlarakReviveBeacon',
    'VoidRayTaldarim',  # Destroyers that spawn with the Mothership
    'AlarakSupplicantWarpTrainDummy',  # actual supplicants show up as well
    'AlarakSupplicantWarpTrainCreator',

    # Nova
    'NovaBoombot',
    'NovaCoopDecoy',
    'NovaReviveBeacon',
    'SpiderMineBurrowed',
    'HealingDrone',
    'Marine_BlackOps',
    'Ghost_BlackOps',
    'GhostFemale_BlackOps',
    'Liberator_BlackOps',
    'Raven_BlackOps',
    'Goliath_BlackOps',
    'SiegeTank_BlackOps',
    'HellbatBlackOps',
    'Marauder_BlackOps',
    'Banshee_BlackOps',

    # Stukov
    # More accurate to track when cocoons started
    'SISCV',
    'SIOverlord',
    'SICocoonInfestedCivilian',
    'SIInfestedTrooper',
    'SIInfestedCivilian',
    'InfestedCivilianPlaceholder',
    'StukovInfestBroodling',
    'SIInfestedMarine',
    'SIInfestedDiamondback',  # TODO verify
    'SIInfestedSiegeTank',  # TODO verify
    'SIInfestedLiberator',  # TODO verify
    'StukovInfestedBanshee',
    'SIBroodQueen',  # TODO verify
    'StukovApocalisk',  # Calldown
    'SIVolatileInfested',  # not sure what this is but couldn't see it in-game
    'StukovAleksander',  # Calldown
    'ALEKSANDERCRASH_PLACEHOLDER',  # Calldown

    # Fenix
    # Fenix Hero Units
    'FenixCoop',
    'FenixDragoon',
    'FenixArbiter',
    # Purifier Conclave
    'FenixAdeptShade',
    'FenixTalisAdeptPhaseShift',
    'FenixChampionTaldarinImmortal',
    'FenixChampionWarbringerColossus',
    'FenixClolarionInterceptor',
    'FenixClolarionBomber',

    # Dehaka
    'EssencePickup',
    'DehakaCoopReviveCocoonFootPrint',
    'DehakaLocust',
    'LocustMPPrecursor',
    'DehakaNydusDestroyerTimedNoFood',
    'DehakaPlacement',
    'NydusDestroyerDeepTunnelPlacement',
    'GreaterNydusDestroyerDeepTunnelPlacement',
    'DehakaCreeperFlying',
    # Calldowns
    'DehakaGlevig',
    'DehakaGlevigDeepTunnelPlacement',
    'CoopDehakaGlevigEggHydralisk',
    'CoopDehakaGlevigEggRoach',
    'CoopDehakaGlevigEggZergling',
    'DehakaMurvar',
    'DehakaDakrun',
    # using cocoons instead
    'DehakaDrone',
    'DehakaZerglingLevel2',
    'DehakaRoachLevel2',
    'DehakaHydraliskLevel2',
    'DehakaSwarmHost',
    'DehakaUltraliskLevel2',

    # Han and Horner
    'HHScrapPickup',
    'HHMagneticMine_SpawnerUnit',
    'HHMagneticMinePrep',
    'HHD8SingleCluster',
    'HHD8ClusterBomb',
    'HHD8CenterCluster',
    'HHWraith',
    'HHVikingFighter',
    'HHRaven',
    'HHBattlecruiser',
    'HHBomber',  # calldown
    'HHMercenarySpaceStation',
    'HHGriffon',
    'HornerAirFleetTargeter',
    'HornerAirFleetStrafer',
])

BO_CHANGED_EXCLUDED = BO_CHANGED_EXCLUDED.copy()

BO_CHANGED_EXCLUDED.update([
    # speculative
    'HHWidowMine',
    'HHVikingAssault',
    'HHVikingFighter',
    'HHViking',
    'HotsRaptor',
    'HotSSwarmling',
    'HHReaper',
])



BO_UPGRADES_EXCLUDED = BO_UPGRADES_EXCLUDED.copy()

BO_UPGRADES_EXCLUDED.update([
    'SprayTerran',
    'SprayProtoss',
    'SprayZerg',
    # Co-op
    'GameTimeGreaterthan5Seconds',
    'NydusNetworkCoopAllyLeft',
    # Vorazun
    'MasteryVorazunTimeStopHasteModifyPlayer',
    # Dehaka
    'DehakaCoopStage2',
    'DehakaColossusLegs',
    'DehakaCoopStage3',
    'DehakaAirAttackUpgrade',
    # Fenix
    'FenixNetworkedSuperiorityZealot',
    'FenixNetworkedSuperiorityAdept',
    'FenixNetworkedSuperiorityImmortal',
    'FenixNetworkedSuperiorityColossus',
    'FenixNetworkedSuperiorityScout',
    'FenixNetworkedSuperiorityCarrier',
])

BUILD_DATA = BUILD_DATA.copy()

BUILD_DATA.update({
    # shared across at least Kerrigan and Zagara
    'overlordspeed': {
        'build_time': 60,  # TODO verify
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        'display_name': 'Pneumatized Carapace',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'overlordtransport': {
        'build_time': 60,  # TODO verify
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        'display_name': 'Ventral Sacs',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'zerglingmovementspeed': {
        'build_time': 60,
        'built_from': ['SpawningPool'],
        'display_name': 'Metabolic Boost',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'HotSZerglingHealth': {
        'build_time': 60,
        'built_from': ['SpawningPool'],
        'display_name': 'Hardened Carapace',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'zerglingattackspeed': {
        'build_time': 60,
        'built_from': ['SpawningPool'],
        'display_name': 'Adrenal Overload',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'ZerglingArmorShred': {
        'build_time': 90,
        'built_from': ['SpawningPool'],
        'display_name': 'Shredding Claws',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'QueenCoop': {
        'build_time': 50,
        'built_from': ['Hatchery', 'Lair', 'Hive'],
        'display_name': 'Queen',
        'race': 'Zerg',
        'type': 'Unit',
        'is_morph': False,
    },
    'VoidCoopHeroicFortitude': {
        'build_time': 60,
        'built_from': ['EvolutionChamber'],
        'display_name': 'Heroic Fortitude',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'ChitinousPlating': {
        'build_time': 60,
        'built_from': ['UltraliskCavern'],
        'display_name': 'Chitinous Plating',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'BurrowCharge': {  # TODO verify
        'build_time': 60,  # TODO verify
        'built_from': ['UltraliskCavern'],
        'display_name': 'Burrow Charge',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'HotSTissueAssimilation': {
        'build_time': 60,
        'built_from': ['UltraliskCavern'],
        'display_name': 'Tissue Assimilation',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    # Kerrigan and Abathur
    'HotSRapidRegeneration': {
        'build_time': 60,
        'built_from': ['Spire', 'GreaterSpire'],
        'display_name': 'Rapid Regeneration',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'MutaliskSunderingGlave': {
        'build_time': 120,
        'built_from': ['Spire', 'GreaterSpire',],
        'display_name': 'Sundering Glave',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'HotSViciousGlaive': {
        'build_time': 90,
        'built_from': ['Spire', 'GreaterSpire'],
        'display_name': 'Vicious Glave',
        'race': 'Zerg',
        'type': 'Upgrade',
        'is_morph': False,
    },
    # Artanis and Karax
    'ImmortalAiur': {
        'build_time': 55,
        'built_from': ['RoboticsFacility'],
        'display_name': 'Immortal',
        'race': 'Protoss',
        'type': 'Unit',
        'is_morph': False,
    },
    # Shared by at least Fenix and Karax
    'Charge': {
        'build_time': 60,
        'built_from': ['TwilightCouncil'],
        'display_name': 'Charge',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'ObserverGraviticBooster': {
        'build_time': 60,
        'built_from': ['RoboticsBay'],
        'display_name': 'Gravitic Boosters',
        'race': 'Protoss',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'ExtendedThermalLance': {
        'build_time': 90,
        'built_from': ['RoboticsBay'],
        'display_name': 'Extended Thermal Lance',
        'race': 'Protoss',
        'type': 'Upgrade',
        'is_morph': False,
    },
    # at least Nova
    'HighCapacityBarrels': {
        'build_time': 60,
        'built_from': ['TechLab'],
        'display_name': 'Infernal Pre-Igniter',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False,
    },
    # Nova and Swann
    'AutomatedRefinery': {
        'build_time': 0,
        'built_from': [],
        'display_name': 'Refinery',
        'race': 'Terran',
        'type': 'Building',
        'is_morph': False,
    },
    'AresClassWeaponsSystem': {
        'build_time': 60,
        'built_from': ['TechLab'],
        'display_name': 'Ares-Class Targeting System',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False,
    },
    'TerranBuildingArmor': {
        'build_time': 60,  # TODO confirm
        'built_from': ['Engineering'],
        'display_name': 'Building Armor',
        'race': 'Terran',
        'type': 'Upgrade',
        'is_morph': False,
    },

})

COMMANDER_BUILD_DATA = {

    'Raynor': {
        # Units
        # Rapid Recruitment halves all build times
        'Marine': {
            'build_time': 13,
            'built_from': ['Barracks'],
            'display_name': 'Marine',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Marauder': {
            'build_time': 15,
            'built_from': ['Barracks'],
            'display_name': 'Marauder',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
            },
        'Firebat': {
            'build_time': 15,
            'built_from': ['Barracks'],
            'display_name': 'Firebat',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Medic': {
            'build_time': 13,
            'built_from': ['Barracks'],
            'display_name': 'Medic',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Vulture': {
            'build_time': 13,
            'built_from': ['Factory'],
            'display_name': 'Vulture',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'SiegeTank': {
            'build_time': 23,
            'built_from': ['Factory'],
            'display_name': 'Siege Tank',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'VikingFighter': {
            'build_time': 21,
            'built_from': ['Starport'],
            'display_name': 'Viking',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Banshee': {
            'build_time': 30,
            'built_from': ['Starport'],
            'display_name': 'Banshee',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Battlecruiser': {
            'build_time': 45,
            'built_from': ['Starport'],
            'display_name': 'Battlecruiser',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings
        'SupplyDepotDrop': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Supply Depot',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },

        # Upgrades
        'StabilizerMedPacks': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Stabilizer Medpacks',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FirebatJuggernautPlating': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Juggernaut Plating',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'BearclawNozzles': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Incinerator Gauntlets',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RaynorTalentedTerranInfantryArmorLevel1': {
            'build_time': 160,
            'built_from': ['EngineeringBay'],
            'display_name': 'Terran Infantry Armor Level 1',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RaynorTalentedTerranInfantryArmorLevel2': {
            'build_time': 190,
            'built_from': ['EngineeringBay'],
            'display_name': 'Terran Infantry Armor Level 2',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RaynorTalentedTerranInfantryArmorLevel3': {
            'build_time': 220,
            'built_from': ['EngineeringBay'],
            'display_name': 'Terran Infantry Armor Level 3',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'NanoConstructor': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Replenishable Magazine',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'CerberusMines': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Cerberus Mines',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AresClassWeaponsSystemViking': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Phobos Weapons System',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RaynorImprovedSiegeMode': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Advanced Siege Tech',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'VehicleAfterburners': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Afterburners',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HALORockets': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Ripwave Missiles',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SwannCommanderVehicleWeaponRange': {
            'build_time': 120,
            'built_from': ['TechLab'],
            'display_name': 'Advanced Optics',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'ClusterWarheads': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Advanced Optics',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RaynorTalentedTerranVehicleAndShipPlatingLevel1': {
            'build_time': 160,
            'built_from': ['Armory'],
            'display_name': 'Terran Vehicle And Ship Armor Level 1',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RaynorTalentedTerranVehicleAndShipPlatingLevel2': {
            'build_time': 190,
            'built_from': ['Armory'],
            'display_name': 'Terran Vehicle And Ship Armor Level 2',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RaynorTalentedTerranVehicleAndShipPlatingLevel3': {
            'build_time': 220,
            'built_from': ['Armory'],
            'display_name': 'Terran Vehicle And Ship Armor Level 3',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Kerrigan': {
        # Units
        # TODO extra Zerglings in the build order?
        'HotSRaptor': {
            'build_time': 24,
            'built_from': [],
            'display_name': 'Zergling',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'Hydralisk': {
            'build_time': 30,
            'built_from': [],
            'display_name': 'Hydralisk',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
            },
        'HydraliskLurker': {
            'build_time': 24,
            'built_from': [],
            'display_name': 'Hydralisk',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'Lurker': {
            'build_time': 15,
            'built_from': ['Hydralisk'],
            'display_name': 'Lurker',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },
        'HotSTorrasque': {
            'build_time': 55,
            'built_from': [],
            'display_name': 'Ultralisk',  # Torrasque strain
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings
        'GreaterNydusWorm': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Omega Worm',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },

        # Upgrades
        'K5ChainLightning': {
            'build_time': 90,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Chain Reaction',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'K5Cooldowns': {
            'build_time': 120,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Ability Efficiency',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'hydraliskspeed': {
            'build_time': 60,
            'built_from': ['HydraliskDen'],
            'display_name': 'Muscular Augments',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HotSHydraliskHealth': {
            'build_time': 90,
            'built_from': ['HydraliskDen'],
            'display_name': 'Ancillary Carapace',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HydraliskFrenzy': {
            'build_time': 120,
            'built_from': ['HydraliskDen'],
            'display_name': 'Frenzy',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SeismicSpines': {
            'build_time': 120,
            'built_from': ['HydraliskDen'],
            'display_name': 'Seismic Spines',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'PorousCartilage': {  # TODO verify
            'build_time': 60,
            'built_from': ['Spire', 'GreaterSpire',],
            'display_name': 'Porous Cartilage',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Artanis': {
        # Units
        'ZealotAiur': {
            'build_time': 38,
            'built_from': ['Gateway', 'WarpGate'],  # warpgate is necessary because of changing types
            'display_name': 'Zealot',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'Dragoon': {
            'build_time': 42,
            'built_from': ['Gateway', 'WarpGate'],  # warpgate is necessary because of changing types
            'display_name': 'Dragoon',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'PhoenixAiur': {
            'build_time': 35,
            'built_from': ['Stargate'],
            'display_name': 'Phoenix',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings

        # Upgrades
        'ZealotResearchWhirlwind': {
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Whirlwind',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'StalkerResearchDragoonRange': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Singularity Charge',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'StalkerResearchDragoonHealth': {
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Trillic Compresion Mesh',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'ImmortalResearchBarrierAdvanced': {
            'build_time': 60,
            'built_from': ['RoboticsBay'],
            'display_name': 'Improved Barrier',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Scarab Housing
        # TODO Solarite Payload
        'HighTemplarKhaydarinAmulet': {
            'build_time': 120,
            'built_from': ['TemplarArchives'],
            'display_name': 'Khaydarin Amulet',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HealingPsionicStorm': {
            'build_time': 90,
            'built_from': ['TemplarArchives'],
            'display_name': 'Plasma Surge',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'TempestDisintegration': {
            'build_time': 90,
            'built_from': ['FleetBeacon'],
            'display_name': 'Disintegration',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Swann': {
        # Units
        # SCVs now benefits from the Level 1 Vehicle Specialist upgrade, which reduces the SCV's build time by 20%.
        'SCV': {
            'build_time': 14,  # TODO verify change in April 2018
            'built_from': ['CommandCenter'],
            'display_name': 'SCV',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Hellbat': {
            'build_time': 24,
            'built_from': ['Factory'],
            'display_name': 'Hellbat',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Goliath': {
            'build_time': 32,
            'built_from': ['Factory'],
            'display_name': 'Goliath',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'SiegeTank': {
            'build_time': 36,
            'built_from': ['Factory'],
            'display_name': 'Siege Tank',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Cyclone': {
            'build_time': 36,
            'built_from': ['Factory'],
            'display_name': 'Cyclone',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Thor': {
            'build_time': 48,
            'built_from': ['Factory'],
            'display_name': 'Thor',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Hellion': {
            'build_time': 24,
            'built_from': ['Factory'],
            'display_name': 'Hellion',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Wraith': {
            'build_time': 40,
            'built_from': ['Starport'],
            'display_name': 'Wraith',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Hercules': {
            'build_time': 32,
            'built_from': ['Starport'],
            'display_name': 'Hercules',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'ScienceVessel': {
            'build_time': 48,
            'built_from': ['Starport'],
            'display_name': 'Science Vessel',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings
        'KelMorianGrenadeTurret': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Devastation Turret',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },
        'PerditionTurret': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Perdition Turret',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },

        # Upgrades
        'HellbatHellArmor': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Infernal Plating',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'MultilockTargetingSystems': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Multi-Lock Weapons System',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'MaelstromRounds': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Maelstrom Rounds',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'CycloneLockOnRangeUpgrade': {
            'build_time': 60,  # reduced ~ April 2018
            'built_from': ['TechLab'],
            'display_name': 'Targeting Optics',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Mag-Field Accelerator now 90s
        # TODO 330mm Barrage Cannon
        'WraithImprovedBurstLaser': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Pulse Amplifier',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Displacement FIeld
        'ScienceVesselFreeRepair': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Improved Nano-Repair',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'ScienceVesselResearchDefensiveMatrix': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Defensive Matrix',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DrakkenLaserDrillBFG': {
            'build_time': 190,
            'built_from': [],  # ?
            'display_name': 'Upgrade Laser Drill Level 1',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DrakkenLaserDrillNuke': {
            'build_time': 220,
            'built_from': [],  # ?
            'display_name': 'Upgrade Laser Drill Level 2',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Zagara': {
        # Units
        'Drone': {
            'build_time': 26,
            'built_from': [],
            'display_name': 'Drone',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'Zergling': {
            'build_time': 9,
            'built_from': [],
            'display_name': 'Zergling',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'HotSSwarmling': {  # Zergling evolution
            'build_time': 2,
            'built_from': [],
            'display_name': 'Swarmling',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'InfestedAbomination': {
            'build_time': 12,
            'built_from': [],
            'display_name': 'Aberration',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'Scourge': {
            'build_time': 12,
            'built_from': [],
            'display_name': 'Scourge',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'Corruptor': {
            'build_time': 16,
            'built_from': [],
            'display_name': 'Corruptor',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },

        # Upgrades
        'ZagaraVoidCoopAttackUpgrade': {
            'build_time': 90,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Medusa Blades',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Protective Cover
        'HotSBanelingCorrosiveBile': {
            'build_time': 90,
            'built_from': ['BanelingNest'],
            'display_name': 'Corrosive Acid',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HotSRupture': {
            'build_time': 90,
            'built_from': ['BanelingNest'],
            'display_name': 'Rupture',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'ScourgeGasCostReduction': {
            'build_time': 60,
            'built_from': ['ScourgeNest'],
            'display_name': 'Simplified Genome',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'ScourgeSplashDamage': {
            'build_time': 60,
            'built_from': ['ScourgeNest'],
            'display_name': 'Virulent Spores',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Vorazun': {
        # Units
        # TODO verify
        'StalkerShakuras': {
            'build_time': 42,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Stalker',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'DarkTemplarShakuras': {
            'build_time': 55,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Dark Templar',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings

        # Upgrades
        'DarkTemplarResearchShadowDash': {
            'build_time': 100,  # wikia was incorrect and had 60 when I last checked
            'built_from': ['DarkShrine'],
            'display_name': 'Blink',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DarkTemplarResearchShadowFury': {
            'build_time': 120,
            'built_from': ['DarkShrine'],
            'display_name': 'Shadow Fury',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'StalkerResearchBlinkShieldRestore': {
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Phase Reactor',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'CorsairMP': {
            'build_time': 35,
            'built_from': ['Stargate'],
            'display_name': 'Corsair',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'CorsairPermanentCloak': {
            'build_time': 90,
            'built_from': ['FleetBeacon'],
            'display_name': 'Stealth Drive',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'CorsairDisruptionWeb': {
            'build_time': 60,
            'built_from': ['FleetBeacon'],
            'display_name': 'Disruption Web',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Karax': {
        # Units
        'ZealotPurifier': {
            'build_time': 38,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Sentinel',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
            },
        'SentryPurifier': {
            'build_time': 37,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Energizer',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
            },
        'ColossusPurifier': {
            'build_time': 75,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Immortal',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
            },
        'PhoenixPurifier': {
            'build_time': 35,
            'built_from': ['Stargate'],
            'display_name': 'Mirage',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
            },
        'CarrierAiur': {
            'build_time': 120,
            'built_from': ['Stargate'],
            'display_name': 'Carrier',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings
        'KhaydarinMonolith': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Khaydarin Monolith',
            'race': 'Protoss',
            'type': 'Building',
            'is_morph': False,
        },

        # Upgrades
        'SolarEfficiencyLevel1': {
            'build_time': 90,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Efficiency Level 1',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SolarEfficiencyLevel2': {
            'build_time': 120,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Efficiency Level 2',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SolarEfficiencyLevel3': {
            'build_time': 180,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Efficiency Level 3',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SOARepairBeamExtraTarget': {
            'build_time': 90,
            'built_from': ['SolarForge'],
            'display_name': 'Advanced Repair Systems',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SOAOrbitalStrikeUpgrade': {
            'build_time': 120,
            'built_from': ['SolarForge'],
            'display_name': 'Phase Detonation',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SOASolarLanceUpgrade': {
            'build_time': 120,
            'built_from': ['SolarForge'],
            'display_name': 'Solar Flare',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Enhanced Targeting 120
        # TODO Optimized Ordinance 120
        # TODO Fortificiation Barrier 60
        'Reconstruction': {  # TODO verify
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Reconstruction',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RapidRecharging': {  # TODO verify
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Rapid Recharging',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'Reclamation': {  # TODO verify
            'build_time': 120,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Reclamation',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Fire Beam 120
        # TODO Shadow Cannon 120
        'PhoenixRangeUpgrade': {
            'build_time': 60,
            'built_from': ['FleetBeacon'],
            'display_name': 'Anion Pulse-Crystals',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'PhasingArmor': {  # TODO verify
            'build_time': 90,
            'built_from': ['FleetBeacon'],
            'display_name': 'Phasing Armor',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'CarrierRepairDrones': {
            'build_time': 120,
            'built_from': ['FleetBeacon'],
            'display_name': 'Repair Drones',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Abathur': {
        # Units
        'RoachVile': {
            'build_time': 27,
            'built_from': [],
            'display_name': 'Roach',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'RavagerAbathur': {
            'build_time': 9,
            'built_from': [],
            'display_name': 'Ravager',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },
        'Brutalisk': {  # actually the cocoon morph from roach
            'build_time': 5,
            'built_from': [],
            'display_name': 'Brutalisk',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },
        'HotSLeviathan': {  # actually the cocoon morph from mutalisk
            'build_time': 5,
            'built_from': [],
            'display_name': 'Leviathan',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },
        'Devourer': {
            'build_time': 15,
            'built_from': [],
            'display_name': 'Devourer',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },

        # Buildings

        # Upgrades
        'AbathurBioMechanicalTransfusion': {
            'build_time': 60,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Bio-Mechanical Transfusion',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HotSRoachDamage': {
            'build_time': 110,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Hydriodic Bile',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Adaptive Plating
        'RavagerCorrosiveBileRadiusIncrease': {
            'build_time': 90,
            'built_from': ['EvolutionChamber'],
            'display_name': 'Bloated Bile Ducts',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Potent Bile
        # TODO Prolonged Dispersion
        'DevourerAoEDamage': {
            'build_time': 90,
            'built_from': ['Spire', 'GreaterSpire'],
            'display_name': 'Corrosive Spray',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HotSPressurizedGlands': {
            'build_time': 90,
            'built_from': ['InfestationPit'],
            'display_name': 'Pressurized Glands',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Virulent Microbes
        # TODO Deep TUnnel
        # TODO Paralytic Barbs
    },

    'Alarak': {
        # Units
        'Supplicant': {
            'build_time': 28,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Supplicant',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'Monitor': {
            'build_time': 37,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Havoc',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'HighTemplarTaldarim': {
            'build_time': 55,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Ascendant',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'ImmortalTaldarim': {
            'build_time': 55,
            'built_from': ['Robotics Facility'],
            'display_name': 'Vanguard',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'WarpPrismTaldarim': {
            'build_time': 50,
            'built_from': ['Robotics Facility'],
            'display_name': 'Warp Prism',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'ColossusTaldarim': {
            'build_time': 75,
            'built_from': ['RoboticsFacility'],
            'display_name': 'Wraithwalker',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'SOAMothershipv4': {
            'build_time': 120,
            'built_from': ['Stargate'],
            'display_name': 'Mothership',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        # Buildings
        'TemplarArchive': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Ascendant Archives',
            'race': 'Protoss',
            'type': 'Building',
            'is_morph': False,
        },
        # Upgrades
        'AlarakAttackStunUpgrade': {
            'build_time': 90,  # TODO Verify
            'built_from': ['Forge'],
            'display_name': 'Imposing Presence',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Telekinesis
        'AlarackHavocPermanentCloak': {
            'build_time': 60,
            'built_from': ['CyberneticsCore'],
            'display_name': 'Cloaking Module',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AlarakHavocAbilityRange': {
            'build_time': 90,
            'built_from': ['CyberneticsCore'],
            'display_name': 'Bloodshard Resonance',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AlarakHavocTargetLockBuff': {
            'build_time': 90,
            'built_from': ['CyberneticsCore'],
            'display_name': 'Detect Weakness',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AlarakSupplicantShieldArmor': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Blood Shields',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AlarakSupplicantMaxShields': {
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Soul Augmentation',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AlarakStalkerPhasingArmor': {
            'build_time': 90,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Phasing Armor',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'VanguardArmoredDamage': {
            'build_time': 60,
            'built_from': ['RoboticsBay'],
            'display_name': 'Fusion Mortars',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Matter Dispersion
        'AlarakColossusChargedBlastAirAttack': {
            'build_time': 60,
            'built_from': ['RoboticsBay'],
            'display_name': 'Aerial Tracking',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AlarakColossusChargedBlastChargeTime': {
            'build_time': 60,  # TODO verify
            'built_from': ['RoboticsBay'],
            'display_name': 'Rapid Power Cycling',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AlarakHighTemplarImprovedSacrifice': {
            'build_time': 60,
            'built_from': ['TemplarArchive'],
            'display_name': 'Power Overwhelming',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'VoidHighTemplarMindBlast': {
            'build_time': 60,
            'built_from': ['TemplarArchive'],
            'display_name': 'Mind Blast',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AlarakHighTemplarPsionicOrbTravelDistance': {
            'build_time': 60,
            'built_from': ['TemplarArchive'],
            'display_name': 'Chaotic Attunement',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Nova': {
        # Units
        'Marine_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Barracks'],
            'display_name': 'Elite Marine',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Marauder_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Barracks'],
            'display_name': 'Hellbat Rangers',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Ghost_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Barracks'],
            'display_name': 'Spec Ops Ghost',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Hellbat_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Factory'],
            'display_name': 'Hellbat Rangers',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Goliath_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Factory'],
            'display_name': 'Strike Goliath',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'SiegeTank_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Factory'],
            'display_name': 'Heavy Siege Tank',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Liberator_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Starport'],
            'display_name': 'Raid Liberator',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Raven_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Starport'],
            'display_name': 'Raven Type-II',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'Banshee_BlackOpsSpawnerUnit': {
            'build_time': 0,  # calldown
            'built_from': ['Starport'],
            'display_name': 'Covert Banshee',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings
        'NovaACLaserTurret': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Railgun Turret',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },
        'GhostAcademyNova': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Ghost Academy',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },
        # Upgrades
        'LaserTargetingSystemNova': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Laser Targeting System',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'MarineSuperStim': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Super Stimpack',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'NovaConcussiveShells': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Suppression Shells',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'MarauderMagrailMunitions': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Suppression Shells',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'GhostBlackOpsEMP': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'EMP Round',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'GhostBlackOpsTripleTap': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Triple Tap',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HellbatJumpJetAssault': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Jump Jet Assault',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'NovaUnitLockdown': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Lockdown Missiles',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DeploySpiderMines': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Spider Mines',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SiegeTankSiegeModeProgressiveRangeIncease': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Graduating Range',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'BansheePermaCloak': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Advanced Cloaking Field',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'BansheeAirstrike': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Rocket Barrage',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'LiberatorStructureAttack': {
            'build_time': 60,
            'built_from': ['TechLab'],
            'display_name': 'Raid Artillery',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'MultiTaskMAFServosLiberator': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Smart Servos',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HealingDroneCloakHealBeam': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Covert Triage',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'RavenSuperScience': {
            'build_time': 90,
            'built_from': ['TechLab'],
            'display_name': 'Enhanced Manufacturing',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'NovaDetector': {
            'build_time': 90,
            'built_from': ['GhostAcademyNova'],
            'display_name': 'Ghost Visor',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'NovaLifeRegen': {
            'build_time': 90,
            'built_from': ['GhostAcademyNova'],
            'display_name': 'Caduceus Reactor',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'NovaSnipeRefund': {
            'build_time': 120,
            'built_from': ['GhostAcademyNova'],
            'display_name': 'Operational Efficiency',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'NovaShotgunBlastRange': {
            'build_time': 120,
            'built_from': ['GhostAcademyNova'],
            'display_name': 'Infernal Projectiles',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Stukov': {
        # Units
        # Track cocoons instead of units for more accurate start times
        'SICocoonInfestedSCV': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested SCV',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'SICocoonInfestedOverlord': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Overlord',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'SICocoonInfestedMarine': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested Marine',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'SICocoonInfestedDiamondback': {  # TODO verify
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested Diamondback',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'SICocoonInfestedSiegeTank': {  # TODO verify
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested Siege Tank',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'SICocoonInfestedLiberator': {  # TODO verify
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested Liberator',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'SICocoonInfestedBanshee': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Infested Banshee',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'SICocoonBroodQueen': {  # TODO verify
            'build_time': 0,
            'built_from': [],
            'display_name': 'Brood Queen',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings

        # Upgrades
        'HeavyInfestation': {
            'build_time': 90,
            'built_from': ['SICommandCenter'],
            'display_name': 'Aggressive Incubation',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SIBarracksTrainInfestedCivilianLevel2': {
            'build_time': 120,
            'built_from': ['SIColonistCompound'],  # TODO verify
            'display_name': 'Infestation Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SIBarracksTrainInfestedCivilianLevel3': {
            'build_time': 120,
            'built_from': ['SIColonistCompound'],  # TODO verify
            'display_name': 'Infestation Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SIBarracksTrainInfestedCivilianLevel4': {
            'build_time': 120,
            'built_from': ['SIColonistCompound'],  # TODO verify
            'display_name': 'Infestation Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'StukovInfestedInfestedCivilianLeapAttack': {
            'build_time': 60,
            'built_from': ['SIColonistCompound'],  # TODO verify
            'display_name': 'Anaerobic Enhancement',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'StukovInfestedCivilianSpawnBroodlingOnDeath': {  # TODO verify
            'build_time': 90,
            'built_from': ['SIColonistCompound'],  # TODO verify
            'display_name': 'Broodling Gestation',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SIMarinePlaguedMunitions': {
            'build_time': 90,
            'built_from': ['SIBarracksTechLab'],
            'display_name': 'Plagued Munitions',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SIMarineTrooperRange': {
            'build_time': 60,
            'built_from': ['SIBarracksTechLab'],
            'display_name': 'Retinal Augmentation',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SIBunkerLifeRegen': {
            'build_time': 60,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Regenerative Plating',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SIBunkerArmor': {
            'build_time': 60,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Calcified Armor',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'SIInfantryWeaponsLevel1': {
            'build_time': 160,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Weapons Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SIInfantryWeaponsLevel2': {
            'build_time': 190,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Weapons Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SIInfantryWeaponsLevel3': {
            'build_time': 220,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Weapons Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SIInfantryArmorLevel1': {
            'build_time': 160,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Armor Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SIInfantryArmorLevel2': {
            'build_time': 190,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Armor Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SIInfantryArmorLevel3': {
            'build_time': 220,
            'built_from': ['SIEngineeringBay'],
            'display_name': 'Stukov Infantry Armor Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        # TODO Stukov Factory Tech Lab
        # TODO Stukov Starport Tech Lab
        # TODO StukovInfestedBansheeInfestedLife
        'SITerranVehicleWeaponsLevel1': {
            'build_time': 160,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Weapons Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SITerranVehicleWeaponsLevel2': {
            'build_time': 190,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Weapons Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SITerranVehicleWeaponsLevel3': {
            'build_time': 220,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Weapons Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SITerranVehicleArmorsLevel1': {
            'build_time': 160,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Armor Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SITerranVehicleArmorsLevel2': {
            'build_time': 190,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Armor Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
            },
        'SITerranVehicleArmorsLevel3': {
            'build_time': 220,
            'built_from': ['SIArmory'],
            'display_name': 'Stukov Vehicle and Ship Armor Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Fenix': {
        # Units
        'ZealotPurifier': {
            'build_time': 30,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Legionnaire',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
            },
        'SentryFenix': {
            'build_time': 37,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Sentry',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'AdeptFenix': {
            'build_time': 38,
            'built_from': ['Gateway', 'WarpGate'],
            'display_name': 'Adept',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        'ColossusPurifier': {
            'build_time': 75,
            'built_from': ['RoboticsFacility'],
            'display_name': 'Colossus',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },
        # TODO Disruptor
        'Scout': {
            'build_time': 30,
            'built_from': ['Stargate'],
            'display_name': 'Scout',
            'race': 'Protoss',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings

        # Upgrades
        'FenixSuitAttackDamage': {
            'build_time': 90,
            'built_from': ['Forge'],
            'display_name': 'Purifier Armaments',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AStrongHeart': {
            'build_time': 10,
            'built_from': ['Forge'],
            'display_name': 'A Strong Heart',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixArbiterDetection': {
            'build_time': 60,
            'built_from': ['Forge'],
            'display_name': 'Observation Protocol',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'AdeptFenixShadeSpawn': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Psionic Projection',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixKaldalisCleave': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Empowered Blades',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionTalisAdeptBounceShotUpgrade': {
            'build_time': 60,
            'built_from': ['TwilightCouncil'],
            'display_name': 'Debilitation System',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Cloaknig Module 60
        # TODO Purification Echo 90
        'FenixImmortalDetonationShot': {
            'build_time': 90,
            'built_from': ['RoboticsBay'],
            'display_name': 'Gravimetric Overload',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixWarbringerColossusPowerShot': {
            'build_time': 90,
            'built_from': ['RoboticsBay'],
            'display_name': 'Purification Blast',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixScoutWeaponRange': {
            'build_time': 60,
            'built_from': ['FleetBeacon'],
            'display_name': 'Combat Sensor Array',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionScoutAOEMissiles': {
            'build_time': 60,
            'built_from': ['FleetBeacon'],
            'display_name': 'Suppression Procedure',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionCarrierBombers': {
            'build_time': 90,
            'built_from': ['FleetBeacon'],
            'display_name': 'Interdictors',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionTaldarinImmortal': {
            'build_time': 60,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Taldarin\'s A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionWarbringerColossus': {
            'build_time': 60,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Warbringer\'s A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionKaldalisZealot': {
            'build_time': 40,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Kaldalis\' A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionMojoScout': {
            'build_time': 60,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Mojo\'s A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionTalisAdept': {
            'build_time': 60,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Talis\' A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'FenixChampionClolarionCarrier': {
            'build_time': 60,
            'built_from': ['PurifierConclave'],  # TODO verify
            'display_name': 'Clolarion\'s A.I. Personality',
            'race': 'Protoss',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },

    'Dehaka': {
        # Units
        'DehakaTrainEggDrone': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Drone',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaTrainEggZergling': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Zergling',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaRavasaur': {  # Zergling morph
            'build_time': 8,
            'built_from': [],
            'display_name': 'Ravasaur',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },
        'DehakaTrainEggRoach': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Roach',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaRoachLevel3': {
            'build_time': 8,
            'built_from': [],
            'display_name': 'Primal Igniter',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },
        'DehakaTrainEggHydralisk': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Hydralisk',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaMutaliskLevel3FightMorph': {  # morph from Hydralisk
            'build_time': 8,
            'built_from': [],
            'display_name': 'Primal Mutalisk',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': True,
        },
        'DehakaTrainEggSwarmHost': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Swarm Host',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },
        'DehakaTrainEggUltralisk': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Ultralisk',
            'race': 'Zerg',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings
        'DehakaBarracks': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Warden',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        'DehakaHatchery': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Hive',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        'DehakaGlevigStructure': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Glevig\'s Den',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        'DehakaMurvarStructure': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Murvar\'s Den',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        'DehakaDakrunStructure': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Dakrun\'s Den',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },
        'DehakaNydusDestroyer': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Primal Wurm',
            'race': 'Zerg',
            'type': 'Building',
            'is_morph': False,
        },

        # Upgrades
        'DehakaPrimalWeaponsLevel1': {
            'build_time': 160,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Attacks Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaPrimalWeaponsLevel2': {
            'build_time': 190,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Attacks Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaPrimalWeaponsLevel3': {
            'build_time': 220,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Attacks Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaPrimalArmorLevel1': {
            'build_time': 160,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Carapace Level 1',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaPrimalArmorLevel2': {
            'build_time': 190,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Carapace Level 2',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaPrimalArmorLevel3': {
            'build_time': 220,
            'built_from': ['DehakaHatchery'],
            'display_name': 'Primal Carapace Level 3',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaRavasaurVSArmor': {
            'build_time': 60,
            'built_from': ['DehakaGlevigStructure'],
            'display_name': 'Dissolving Acid',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaRavasaurRange': {
            'build_time': 60,
            'built_from': ['DehakaGlevigStructure'],
            'display_name': 'Enlarged Parotid Glands',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaRoachMoveSpeed': {
            'build_time': 60,
            'built_from': ['DehakaGlevigStructure'],
            'display_name': 'Glial Reconstitution',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Concentrated Fire 120
        'DehakaHydraliskSpeed': {
            'build_time': 60,
            'built_from': ['DehakaGlevigStructure'],
            'display_name': 'Muscular Augments',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaImpalerTenderize': {
            'build_time': 60,
            'built_from': ['DehakaGlevigStructure'],
            'display_name': 'Tenderize',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaUltraliskCrashingCharge': {
            'build_time': 60,
            'built_from': ['DehakaDakrunStructure'],
            'display_name': 'Brutal Charge',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaUltraliskRegen': {
            'build_time': 60,
            'built_from': ['DehakaDakrunStructure'],
            'display_name': 'Healing Adaptation',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'DehakaMutaliskAirDoubleDamage': {
            'build_time': 60,
            'built_from': ['DehakaMurvarStructure'],
            'display_name': 'Slicing Glave',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Shifting Carapace 60
        'DehakaMutaliskRespawnOnDeath': {
            'build_time': 90,
            'built_from': ['DehakaMurvarStructure'],
            'display_name': 'Primal Reconstitution',
            'race': 'Zerg',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Explosive Spores 60
        # TODO Primordial Fury 60
    },

    'Horner': {
        # Units
        'HHSCV': {
            'build_time': 17,
            'built_from': ['CommandCenter'],
            'display_name': 'SCV',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHReaper': {
            'build_time': 14,
            'built_from': ['HHMercStarportNoArmy'],
            'display_name': 'Reaper',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHWidowMine': {
            'build_time': 21,
            'built_from': ['HHMercStarportNoArmy'],
            'display_name': 'Widow Mine',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHHellion': {
            'build_time': 14,
            'built_from': ['HHMercStarportNoArmy'],
            'display_name': 'Hellion',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHHellionTank': {
            'build_time': 14,
            'built_from': ['HHMercStarportNoArmy'],
            'display_name': 'Hellbat',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        # Calldowns
        'HHWraith_SpawnerUnit': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Asteria Wraith',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHViking_SpawnerUnit': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Deimos Viking',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHRaven_SpawnerUnit': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Theia Raven',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },
        'HHBattlecruiser_SpawnerUnit': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Sovereign Battlecruiser',
            'race': 'Terran',
            'type': 'Unit',
            'is_morph': False,
        },

        # Buildings
        'HHMercStarportNoArmy': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Assault Galleon',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },
        'HHMercCompound': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Engineering Bay',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },
        'HHBomberPlatform': {
            'build_time': 0,
            'built_from': [],
            'display_name': 'Strike Fighter Platform',
            'race': 'Terran',
            'type': 'Building',
            'is_morph': False,
        },

        # Upgrades
        'HHReaperG4ClusterBombs': {
            'build_time': 60,
            'built_from': ['HHMercCompound'],
            'display_name': 'LE9 Cluster Charges',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHReaperFlight': {
            'build_time': 90,
            'built_from': ['HHMercCompound'],
            'display_name': 'Jetpack Overdrive',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHWidowMineDeathBlossom': {
            'build_time': 60,
            'built_from': ['HHMercCompound'],
            'display_name': 'Executioner Missiles',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHHellionStimDeath': {
            'build_time': 60,
            'built_from': ['HHMercCompound'],
            'display_name': 'Aerosol Stim Emitters',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Black Market Launchers
        'HHHellionFearDeath': {
            'build_time': 60,
            'built_from': ['HHMercCompound'],
            'display_name': 'Wildfire Explosives',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Tar Bombs
        # TODO Immolation Fluid
        'HHWraithPermaCloak': {
            'build_time': 90,
            'built_from': ['StarportTechLab'],
            'display_name': 'Unregistered Cloak System',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Trigger Override
        'HHVikingRockets': {
            'build_time': 90,
            'built_from': ['StarportTechLab'],
            'display_name': 'W.I.L.D. Missiles',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Shredder Rounds
        'FleetwideJump': {
            'build_time': 90,
            'built_from': ['StarportTechLab'],
            'display_name': 'Tactical Jump',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Multi-Threaded Sensors
        'HHVehicleAndShipWeaponsLevel1': {
            'build_time': 160,
            'built_from': ['Armory'],
            'display_name': 'Horner Weapons Level 1',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHVehicleAndShipWeaponsLevel2': {
            'build_time': 190,
            'built_from': ['Armory'],
            'display_name': 'Horner Weapons Level 2',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHVehicleAndShipWeaponsLevel3': {
            'build_time': 220,
            'built_from': ['Armory'],
            'display_name': 'Horner Weapons Level 3',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHVehicleAndShipArmorsLevel1': {
            'build_time': 160,
            'built_from': ['Armory'],
            'display_name': 'Horner Armor Level 1',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHVehicleAndShipArmorsLevel2': {
            'build_time': 190,
            'built_from': ['Armory'],
            'display_name': 'Horner Armor Level 2',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        'HHVehicleAndShipArmorsLevel3': {
            'build_time': 220,
            'built_from': ['Armory'],
            'display_name': 'Horner Armor Level 3',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
        # TODO Overcharged Reactor
        'HHBomberNapalm': {
            'build_time': 90,
            'built_from': ['FusionCore'],
            'display_name': 'Napalm Payload',
            'race': 'Terran',
            'type': 'Upgrade',
            'is_morph': False,
        },
    },
}

# adjust by the FPS
for commander_data in COMMANDER_BUILD_DATA.values():
    for value in commander_data.values():
        value['build_time'] *= FRAMES_PER_SECOND

# take the base data and incorporate commander data
for commander in COMMANDER_BUILD_DATA:
    combined_data = BUILD_DATA.copy()
    combined_data.update(COMMANDER_BUILD_DATA[commander])
    COMMANDER_BUILD_DATA[commander] = combined_data
