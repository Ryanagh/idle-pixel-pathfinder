from idle_pixel_api_client import IdlePixelPlayerLookup


class Pathfinder:
    def __init__(self, username):
        # Found x advancement suggestions, click the following the link to see them in detail: paste bin url
        pass

    def quest_progress(self):
        pass


if __name__ == '__main__':
    player = IdlePixelPlayerLookup("zlef")
    player_data = player.fetch_data()["items_variables"]

    quests = [
      "doric_the_crafter_quest",
      "the_gem_seeker_quest",
      "the_achiever_quest",
      "stardust_expert_quest",
      "combat_tutor_quest",
      "ent_boss_quest",
      "faradoxs_introduction_quest",
      "fisherman_quest",
      "combat_collection_log_quest",
      "tank_boss_quest",
      "thief_leader_quest",
      "dad_goblin_quest",
      "combat_presets_quest",
      "shiny_resources_quest",
      "fire_witch_sister_quest",
      "the_carpenter_quest",
      "the_four_crystals_quest",
      "ghost_miner_boss_quest",
      "bob_the_farmer_quest",
      "junk_collector_quest",
      "the_merchant_quest",
      "junk_planet_quest",
      "faradox_attempt_quest",
      "odd_one_out_quest",
      "the_four_metals_quest",
      "teleport_crystal_quest",
      "pyre_log_priest_quest",
      "train_combat_network_quest",
      "let_us_invent_things_quest",
      "time_warp_chemist_quest",
      "enchanted_birdbath_quest",
      "mega_tablette_quest",
      "tcg_card_collection_quest"]

    for quest in quests:
        print(quest)
        print(player_data.get(quest, 0))
